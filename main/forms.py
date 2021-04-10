from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood, Profile, Post

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants', 'healthline', 'policeline', 'admin')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'hood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post', 'date', 'user', 'hood']
