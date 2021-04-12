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


# class ProjectTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='mimi')
#         self.project = Project.objects.create(title='project', image='https://picture.com', description='description', link='http://url.com')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.project, Project))

#     def test_save_project(self):
#         self.project.save_project()
#         project = Project.objects.all()
#         self.assertTrue(len(project) > 0)

#     def test_get_projects(self):
#         self.project.save()
#         projects = Project.all_projects()
#         self.assertTrue(len(projects) > 0)

#     def test_search_project(self):
#         self.project.save()
#         project = Project.search_project('test')
#         self.assertTrue(len(project) > 0)

#     def test_delete_project(self):
#         self.project.delete_project()
#         project = Project.search_project('test')
#         self.assertTrue(len(project) < 1)