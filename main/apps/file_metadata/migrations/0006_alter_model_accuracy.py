# Generated by Django 4.1.1 on 2024-09-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_metadata', '0005_rename_performance_model_accuracy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='accuracy',
            field=models.FloatField(null=True),
        ),
    ]
