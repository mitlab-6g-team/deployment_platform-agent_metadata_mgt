# Generated by Django 4.1.1 on 2024-09-05 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_metadata', '0004_remove_model_inference_environment_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='performance',
            new_name='accuracy',
        ),
    ]
