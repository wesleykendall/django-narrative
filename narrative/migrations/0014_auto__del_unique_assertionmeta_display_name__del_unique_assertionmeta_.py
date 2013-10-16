# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'EventMeta', fields ['display_name']
        db.delete_unique(u'narrative_eventmeta', ['display_name'])

        # Removing unique constraint on 'EventMeta', fields ['class_load_path']
        db.delete_unique(u'narrative_eventmeta', ['class_load_path'])

        # Removing unique constraint on 'AssertionMeta', fields ['class_load_path']
        db.delete_unique(u'narrative_assertionmeta', ['class_load_path'])

        # Removing unique constraint on 'AssertionMeta', fields ['display_name']
        db.delete_unique(u'narrative_assertionmeta', ['display_name'])

        # Adding unique constraint on 'AssertionMeta', fields ['class_load_path', 'display_name']
        db.create_unique(u'narrative_assertionmeta', ['class_load_path', 'display_name'])

        # Adding unique constraint on 'EventMeta', fields ['class_load_path', 'display_name']
        db.create_unique(u'narrative_eventmeta', ['class_load_path', 'display_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'EventMeta', fields ['class_load_path', 'display_name']
        db.delete_unique(u'narrative_eventmeta', ['class_load_path', 'display_name'])

        # Removing unique constraint on 'AssertionMeta', fields ['class_load_path', 'display_name']
        db.delete_unique(u'narrative_assertionmeta', ['class_load_path', 'display_name'])

        # Adding unique constraint on 'AssertionMeta', fields ['display_name']
        db.create_unique(u'narrative_assertionmeta', ['display_name'])

        # Adding unique constraint on 'AssertionMeta', fields ['class_load_path']
        db.create_unique(u'narrative_assertionmeta', ['class_load_path'])

        # Adding unique constraint on 'EventMeta', fields ['class_load_path']
        db.create_unique(u'narrative_eventmeta', ['class_load_path'])

        # Adding unique constraint on 'EventMeta', fields ['display_name']
        db.create_unique(u'narrative_eventmeta', ['display_name'])


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'narrative.assertionmeta': {
            'Meta': {'unique_together': "(('display_name', 'class_load_path'),)", 'object_name': 'AssertionMeta'},
            'args_json': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'blank': 'True'}),
            'check_interval_seconds': ('django.db.models.fields.IntegerField', [], {'default': '3600'}),
            'class_load_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'})
        },
        u'narrative.datum': {
            'Meta': {'object_name': 'Datum'},
            'datum_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'datum_note_json': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'expiration_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'thread_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'narrative.eventmeta': {
            'Meta': {'unique_together': "(('display_name', 'class_load_path'),)", 'object_name': 'EventMeta'},
            'check_interval_seconds': ('django.db.models.fields.IntegerField', [], {'default': '3600'}),
            'class_load_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'})
        },
        u'narrative.issue': {
            'Meta': {'object_name': 'Issue'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'failed_assertion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['narrative.AssertionMeta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resolved_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'narrative.modelissue': {
            'Meta': {'object_name': 'ModelIssue', '_ormbases': [u'narrative.Issue']},
            u'issue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['narrative.Issue']", 'unique': 'True', 'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'model_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"})
        },
        u'narrative.resolutionstep': {
            'Meta': {'object_name': 'ResolutionStep'},
            'action_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['narrative.Issue']"}),
            'solution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['narrative.Solution']", 'null': 'True', 'blank': 'True'})
        },
        u'narrative.solution': {
            'Meta': {'object_name': 'Solution'},
            'diagnostic_case_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'enacted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'error_traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_json': ('django.db.models.fields.TextField', [], {}),
            'problem_description': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['narrative']