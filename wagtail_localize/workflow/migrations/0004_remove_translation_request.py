# Generated by Django 2.1.15 on 2020-05-25 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_workflow', '0003_remove_translationrequest_target_root'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translationrequestpage',
            name='completed_revision',
        ),
        migrations.RemoveField(
            model_name='translationrequestpage',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='translationrequestpage',
            name='request',
        ),
        migrations.RemoveField(
            model_name='translationrequestpage',
            name='source_revision',
        ),
        migrations.DeleteModel(
            name='TranslationRequest',
        ),
        migrations.DeleteModel(
            name='TranslationRequestPage',
        ),
    ]