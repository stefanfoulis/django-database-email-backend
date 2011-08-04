# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Email'
        db.create_table('database_email_backend_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sent_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('from_email', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('to_emails', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('cc_emails', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('bcc_emails', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('all_recipients', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('headers', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('subject', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('raw', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('database_email_backend', ['Email'])


    def backwards(self, orm):
        
        # Deleting model 'Email'
        db.delete_table('database_email_backend_email')


    models = {
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
