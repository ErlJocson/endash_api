from rest_framework import serializers
from .models import Cards

class CardSerializer(serializers.Serializer):
    class Meta:
        model = Cards
        fields = [
            'id',
            'title',
            'logo',
            'video',
            'link',
            'position',
        ]