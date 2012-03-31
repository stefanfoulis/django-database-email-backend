#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib import admin
from django import forms
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import message
from django.db.models import Count
from django.utils.functional import update_wrapper
from database_email_backend.models import Email, Attachment
from django.utils.translation import ugettext as _

WIDE_INPUT_SIZE = '80'


###################
# view sent email #
###################


class AttachmentInlineAdmin(admin.TabularInline):
    model = Attachment
    extra = 0
    can_delete = False
    max_num = 0
    readonly_fields = ('filename', 'mimetype', 'content', 'file_link',)
    fields = ('file_link', 'mimetype',)

    def file_link(self, obj):
        url_name = '%s:%s_email_attachment' % (self.admin_site.name, self.model._meta.app_label,)
        kwargs={
            'email_id': str(obj.email_id),
            'attachment_id': str(obj.id),
            'filename': str(obj.filename)}
        url = reverse(url_name, kwargs=kwargs)
        return u'<a href="%(url)s">%(filename)s</a>' % {'filename': obj.filename, 'url': url}
    file_link.allow_tags = True


class EmailAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'to_emails', 'subject', 'body_stripped', 'sent_at', 'attachment_count')
    date_hierarchy = 'sent_at'
    search_fields =  ('from_email', 'to_emails', 'subject', 'body',)
    exclude = ('raw',)
    readonly_fields = list_display + ('cc_emails', 'bcc_emails', 'all_recipients', 'headers', 'body',)
    inlines = (AttachmentInlineAdmin,)
    
    def queryset(self, request):
        queryset = super(EmailAdmin, self).queryset(request)
        return queryset.annotate(attachment_count_cache=Count('attachments'))

    def attachment_count(self, obj):
        return obj.attachment_count
    attachment_count.admin_order_field = 'attachment_count_cache'
    
    def body_stripped(self, obj):
        if obj.body and len(obj.body)>100:
            return obj.body[:100] + ' [...]'
        return obj.body
    body_stripped.short_description = 'body'
    body_stripped.admin_order_field = 'body'

    def get_urls(self):
        urlpatterns = super(EmailAdmin, self).get_urls()
        from django.conf.urls.defaults import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        appname = self.model._meta.app_label

        urlpatterns = patterns('',
            url(r'^(?P<email_id>\d+)/attachments/(?P<attachment_id>\d+)/(?P<filename>[\w.]+)$',
                wrap(self.serve_attachment),
                name='%s_email_attachment' % appname)
        ) + urlpatterns
        return urlpatterns

    def serve_attachment(self, request, email_id, attachment_id, filename, extra_context=None):
        if not self.has_change_permission(request, None):
            raise PermissionDenied
        attachment = Attachment.objects.get(email__id=email_id, id=attachment_id, filename=filename)
        response = HttpResponse(attachment.content, mimetype=attachment.mimetype or 'application/octet-stream')
        response["Content-Length"] = len(attachment.content)
        return response

admin.site.register(Email, EmailAdmin)


##############
# send email #
##############


class SendEmail(Email):
    class Meta:
        proxy = True


class SendEmailForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        widgets = {
            'from_email': forms.TextInput(attrs={'size': '30'}),
            'to_emails': forms.TextInput(attrs={'size': WIDE_INPUT_SIZE}),
            'cc_emails': forms.TextInput(attrs={'size': WIDE_INPUT_SIZE}),
            'bcc_emails': forms.TextInput(attrs={'size': WIDE_INPUT_SIZE}),
            'subject': forms.TextInput(attrs={'size': WIDE_INPUT_SIZE}),
        }
        


class SendEmailAdmin(admin.ModelAdmin):
    form = SendEmailForm
    fieldsets = (
        (None, {'fields':('from_email', 'to_emails')}),
        (_('cc and bcc'), {
            'fields': ('cc_emails', 'bcc_emails'),
            'classes': ('collapse',)}),
        (None, {'fields': ('subject', 'body')}),
    )
    
    def save_model(self, request, obj, form, change):
        """
        sends the email and does not save it
        """
        email = message.EmailMessage(
            subject=obj.subject,
            body=obj.body,
            from_email=obj.from_email,
            to=[t.strip() for t in obj.to_emails.split(',')],
            bcc=[t.strip() for t in obj.bcc_emails.split(',')],
            cc=[t.strip() for t in obj.cc_emails.split(',')]
        )
        email.send()

    def response_add(self, request, obj, post_url_continue=None):
        msg = _('The Email was sent successfully.')
        self.message_user(request, msg)
        if "_addanother" in request.POST:
            return HttpResponseRedirect(request.path)
        return HttpResponseRedirect('../../')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_model_perms(self, request):
        return {
            'add': self.has_add_permission(request),
            'change': False,
            'delete': False
        }
admin.site.register(SendEmail, SendEmailAdmin)