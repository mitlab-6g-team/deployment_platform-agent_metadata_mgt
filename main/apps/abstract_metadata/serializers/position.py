from main.apps.abstract_metadata.models.position import Position
from rest_framework import serializers

class PositionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields=['name', 'description', 'port_number', 'inference_client_name', 'deploy_status', 'f_model_uid', 'f_application_uid']

class PositionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields='__all__'
