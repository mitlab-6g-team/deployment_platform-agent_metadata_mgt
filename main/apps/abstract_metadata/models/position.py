from django.db import models
from main.apps.abstract_metadata.models.application import Application
from main.apps.file_metadata.models.model import Model
from uuid import uuid4
import random

def create_port_number():
    while True:
        number = random.randint(35000, 36000)
        if not Position.objects.filter(port_number=number).exists():
            return number


class Position(models.Model):
    uid=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_time=models.DateTimeField(auto_now_add=True, editable=False)
    name=models.CharField(max_length=255, blank=False)
    description=models.TextField(blank=True)
    port_number=models.IntegerField(blank=False, unique=True, default=create_port_number)
    inference_client_name=models.CharField(max_length=255, blank=False, unique=True)
    deploy_status=models.CharField(max_length=255, blank=False, default='Deploying')
    f_model_uid=models.ForeignKey(Model, on_delete=models.CASCADE, to_field='uid')
    f_application_uid=models.ForeignKey(Application, on_delete=models.CASCADE, to_field='uid')

    class Meta:
        db_table="position"
