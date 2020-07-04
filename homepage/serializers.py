from rest_framework import serializers
from .models import TestModel

class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id', 'name', 'code')