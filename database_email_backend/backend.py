#-*- coding: utf-8 -*-
from email.MIMEBase import MIMEBase
from django.core.mail.backends.base import BaseEmailBackend
from database_email_backend.models import Email, Attachment


class DatabaseEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        if not email_messages:
            return
        for message in email_messages:
            email = Email.objects.create(
                from_email = message.from_email,
                to_emails = ', '.join(message.to),
                cc_emails = ', '.join(message.cc),
                bcc_emails = ', '.join(message.bcc),
                all_recipients = ', '.join(message.recipients()),
                subject = message.subject,
                body = message.body,
                raw = message.message().as_string()
            )
            for attachment in message.attachments:
                if isinstance(attachment, tuple):
                    filename, content, mimetype = attachment
                elif isinstance(attachment, MIMEBase):
                    filename = attachment.get_filename()
                    content = attachment.get_payload(decode=True)
                    mimetype = None
                else:
                    continue
                Attachment.objects.create(
                    email=email,
                    filename=filename,
                    content=content,
                    mimetype=mimetype
                )
