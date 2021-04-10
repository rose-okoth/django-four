from django import forms
from .models import Neighborhood

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']