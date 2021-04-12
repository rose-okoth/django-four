from django import forms
from django.contrib.auth.models import User
from .models import Neighborhood, Profile, Post, Business

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'occupants', 'image', 'healthline', 'policeline', 'admin')

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
        fields = ['title', 'post', 'user', 'hood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'description', 'image', 'neighborhood', 'user']