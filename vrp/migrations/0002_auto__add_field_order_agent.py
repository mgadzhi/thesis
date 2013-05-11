# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.agent'
        db.add_column(u'vrp_order', 'agent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=8, to=orm['users.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.agent'
        db.delete_column(u'vrp_order', 'agent_id')


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
        u'users.user': {
            'Meta': {'object_name': 'User'},
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
            'reseller': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'agents'", 'null': 'True', 'to': u"orm['users.User']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'default': "'AG'", 'max_length': '2'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'vrp.depot': {
            'Meta': {'object_name': 'Depot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'vrp.edge': {
            'Meta': {'object_name': 'Edge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'station1'", 'to': u"orm['vrp.Station']"}),
            'station2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'station2'", 'to': u"orm['vrp.Station']"})
        },
        u'vrp.network': {
            'Meta': {'object_name': 'Network'},
            'edges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['vrp.Edge']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vrp.Station']"})
        },
        u'vrp.order': {
            'Meta': {'object_name': 'Order'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vrp.Station']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'vrp.station': {
            'Meta': {'object_name': 'Station'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'vrp.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_capacity': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['vrp']