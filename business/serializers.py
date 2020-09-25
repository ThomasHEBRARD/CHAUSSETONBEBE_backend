from rest_framework import serializers
from .models import BusinessModel


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = '__all__'

