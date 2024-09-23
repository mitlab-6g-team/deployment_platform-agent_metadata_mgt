from django.db import models
from main.apps.abstract_metadata.models.application import Application

class Model(models.Model):
    uid=models.UUIDField(primary_key=True, blank=False)
    created_time=models.DateTimeField(blank=False)
    name=models.CharField(max_length=255, blank=False)
    description=models.TextField(blank=True)
    type=models.CharField(max_length=255, blank=False)
    version=models.FloatField(blank=False)
    accuracy=models.FloatField(null=True)
    access_token=models.CharField(max_length=255, blank=False)
    source=models.UUIDField(blank=True, null=True)
    inference_template_uid=models.UUIDField(blank=False)
    file_extension=models.CharField(max_length=255, blank=True)
    f_application_uid=models.ForeignKey(Application, on_delete=models.CASCADE, to_field='uid')

    class Meta:
        db_table="model"
