from rest_framework import serializers
from ..models import Shows


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'
