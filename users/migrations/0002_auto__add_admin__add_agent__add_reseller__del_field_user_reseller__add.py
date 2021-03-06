# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Admin'
        db.create_table(u'users_admin', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'users', ['Admin'])

        # Adding model 'Agent'
        db.create_table(u'users_agent', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'users', ['Agent'])

        # Adding model 'Reseller'
        db.create_table(u'users_reseller', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'users', ['Reseller'])

        # Deleting field 'User.reseller'
        db.delete_column(u'users_user', 'reseller_id')

        # Adding field 'User.agent_reseller'
        db.add_column(u'users_user', 'agent_reseller',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='agents', null=True, to=orm['users.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Admin'
        db.delete_table(u'users_admin')

        # Deleting model 'Agent'
        db.delete_table(u'users_agent')

        # Deleting model 'Reseller'
        db.delete_table(u'users_reseller')

        # Adding field 'User.reseller'
        db.add_column(u'users_user', 'reseller',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='agents', null=True, to=orm['users.User']),
                      keep_default=False)

        # Deleting field 'User.agent_reseller'
        db.delete_column(u'users_user', 'agent_reseller_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.admin': {
            'Meta': {'object_name': 'Admin', '_ormbases': [u'users.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.agent': {
            'Meta': {'object_name': 'Agent', '_ormbases': [u'users.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.reseller': {
            'Meta': {'object_name': 'Reseller', '_ormbases': [u'users.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'agent_reseller': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'agents'", 'null': 'True', 'to': u"orm['users.User']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'default': "'AG'", 'max_length': '2'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['users']