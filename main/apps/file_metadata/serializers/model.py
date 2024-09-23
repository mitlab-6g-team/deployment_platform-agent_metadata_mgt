from main.apps.file_metadata.models.model import Model
from rest_framework import serializers

class ModelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Model
        fields='__all__'

class ModelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Model
        fields='__all__'
