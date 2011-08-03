#-*- coding: utf-8 -*-
from django.contrib import admin
from database_email_backend.models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'to_emails', 'subject', 'body_stripped', 'sent_at',)
    date_hierarchy = 'sent_at'
    search_fields =  ('from_email', 'to_emails', 'subject', 'body',)
    exclude = ('raw',)

    def body_stripped(self, obj):
        if obj.body and len(obj.body)>100:
            return obj.body[:100] + ' [...]'
        return obj.body
    body_stripped.short_description = 'body'
    body_stripped.admin_order_field = 'body'

admin.site.register(Email, EmailAdmin)

