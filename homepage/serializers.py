from rest_framework import serializers
from .models import HomePageModel


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageModel
        fields = '__all__'

