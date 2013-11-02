# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HelloModel'
        db.create_table(u'mocks_hellomodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mocks', ['HelloModel'])


    def backwards(self, orm):
        # Deleting model 'HelloModel'
        db.delete_table(u'mocks_hellomodel')


    models = {
        u'mocks.hellomodel': {
            'Meta': {'object_name': 'HelloModel'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mocks']