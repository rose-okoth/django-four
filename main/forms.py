from django import forms
from .models import Neighborhood

class NeighborhoodForm():
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants')