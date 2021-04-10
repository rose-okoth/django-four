from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupants = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    healthline = models.IntegerField(null=True, blank=True)
    policeline = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='neighborhood')

    def __str__(self):
        return self.title

    def create_neighborhood(self):
        self.save

    def delete_neighborhood(self):
        self.save

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    hood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
