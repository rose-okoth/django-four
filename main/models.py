from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupants = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    # admin = models.ForeignKey(admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:home", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):

    '''Create slug function'''

    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Neighborhood.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):

    '''Save slug function'''

    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Neighborhood)
