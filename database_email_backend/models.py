#-*- coding: utf-8 -*-
from database_email_backend.fields import Base64Field
from django.db import models


class Email(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    from_email = models.CharField(blank=True, default='', max_length=255)
    to_emails = models.TextField(blank=True, default='')
    cc_emails = models.TextField(blank=True, default='')
    bcc_emails = models.TextField(blank=True, default='')
    all_recipients = models.TextField(blank=True, default='')
    headers =  models.TextField(blank=True, default='')

    subject = models.TextField(blank=True, default='')
    body = models.TextField(blank=True, default='')
    raw = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'Email from "%s" to "%s" sent at %s about "%s"' % (self.from_email, self.to_emails,
                                                                   self.sent_at, self.subject)

    @property
    def attachment_count(self):
        if not hasattr(self, 'attachment_count_cache'):
            self.attachment_count_cache = self.attachments.count()
        return self.attachment_count_cache

class Attachment(models.Model):
    email = models.ForeignKey(Email, related_name='attachments')
    filename = models.CharField(max_length=255, null=True, blank=True, default=None)
    content = Base64Field(null=True, blank=True, default=None)
    mimetype = models.CharField(max_length=255, null=True, blank=True, default=None)