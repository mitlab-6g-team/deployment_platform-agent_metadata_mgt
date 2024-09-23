from main.apps.abstract_metadata.models.topic import Topic
from rest_framework import serializers

class TopicWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields='__all__'
        
class TopicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields='__all__'
