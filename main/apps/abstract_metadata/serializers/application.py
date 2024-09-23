from main.apps.abstract_metadata.models.application import Application
from rest_framework import serializers

class ApplicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'

class ApplicationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'
