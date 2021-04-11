from rest_framework import serializers
from .models import Neighborhood

class HoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location')

class ViewHoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants', 'slug', 'healthline', 'policeline', 'admin')

        
