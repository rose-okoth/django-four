from django.test import TestCase
from .models import *
import datetime as dt
from django.contrib.auth.models import User

class UserTestClass(TestCase):
    def setUp(self):
        self.rose= User(username = 'Rose', password = '123456789')

    def test_instance(self):
        self.assertTrue(isinstance(self.rose,User))


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='mimi', password='passw0rd')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class TestNeighborhood(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='mimi')
        self.neighborhood = Neighborhood.objects.create(
            name='neighborhood', 
            location='location', 
            occupants='2', 
            slug='slug', 
            healthline='700000000', 
            policeline='700000000', 
            image='https://picture.com',
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_save_neighborhood(self):
        self.neighborhood.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def test_create_neighborhoods(self):
        self.neighborhood.save()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_neighborhood(self):
        self.neighborhood.delete_neighborhood()
        neighborhood = Neighborhood.search_neighborhood('test')
        self.assertTrue(len(neighborhood) < 1)
   
