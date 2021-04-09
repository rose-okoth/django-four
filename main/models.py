from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupants = models.CharField(max_length=250)
    # admin = models.ForeignKey(admin, on_delete=models.CASCADE)
