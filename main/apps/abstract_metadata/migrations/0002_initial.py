# Generated by Django 4.1.1 on 2024-08-20 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abstract_metadata', '0001_initial'),
        ('file_metadata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='f_model_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_metadata.model'),
        ),
    ]
