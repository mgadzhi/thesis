# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Depot'
        db.create_table(u'vrp_depot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'vrp', ['Depot'])

        # Adding model 'Station'
        db.create_table(u'vrp_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'vrp', ['Station'])

        # Adding model 'Edge'
        db.create_table(u'vrp_edge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='station1', to=orm['vrp.Station'])),
            ('station2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='station2', to=orm['vrp.Station'])),
        ))
        db.send_create_signal(u'vrp', ['Edge'])

        # Adding model 'Network'
        db.create_table(u'vrp_network', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vrp.Station'])),
        ))
        db.send_create_signal(u'vrp', ['Network'])

        # Adding M2M table for field edges on 'Network'
        db.create_table(u'vrp_network_edges', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('network', models.ForeignKey(orm[u'vrp.network'], null=False)),
            ('edge', models.ForeignKey(orm[u'vrp.edge'], null=False))
        ))
        db.create_unique(u'vrp_network_edges', ['network_id', 'edge_id'])

        # Adding model 'Vehicle'
        db.create_table(u'vrp_vehicle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('max_capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'vrp', ['Vehicle'])

        # Adding model 'Order'
        db.create_table(u'vrp_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vrp.Station'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'vrp', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Depot'
        db.delete_table(u'vrp_depot')

        # Deleting model 'Station'
        db.delete_table(u'vrp_station')

        # Deleting model 'Edge'
        db.delete_table(u'vrp_edge')

        # Deleting model 'Network'
        db.delete_table(u'vrp_network')

        # Removing M2M table for field edges on 'Network'
        db.delete_table('vrp_network_edges')

        # Deleting model 'Vehicle'
        db.delete_table(u'vrp_vehicle')

        # Deleting model 'Order'
        db.delete_table(u'vrp_order')


    models = {
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