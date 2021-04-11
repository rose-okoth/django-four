from rest_framework import serializers
from .models import Neighborhood

class HoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('name')