# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Attachment'
        db.create_table('database_email_backend_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database_email_backend.Email'])),
            ('filename', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('content_base64', self.gf('database_email_backend.fields.Base64Field')(default=None, null=True, db_column='content', blank=True)),
            ('mimetype', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('database_email_backend', ['Attachment'])


    def backwards(self, orm):
        
        # Deleting model 'Attachment'
        db.delete_table('database_email_backend_attachment')


    models = {
        'database_email_backend.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'content_base64': ('database_email_backend.fields.Base64Field', [], {'default': 'None', 'null': 'True', 'db_column': "'content'", 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['database_email_backend.Email']"}),
            'filename': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'database_email_backend.email': {
            'Meta': {'object_name': 'Email'},
            'all_recipients': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'bcc_emails': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'cc_emails': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'from_email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'headers': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'to_emails': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['database_email_backend']
