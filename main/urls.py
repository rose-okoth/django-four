from . import views
from django.urls import path, re_path

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('hoods', views.hood, name="hoods"),
    path('create', views.new_hood, name='create'),
    path('profile', views.user_profile, name='profile'),
    re_path(r'^(?P<slug>[\w-]+)/post/$', views.create_post, name='post'),
    re_path(r'^(?P<slug>[\w-]+)/business/$', views.create_business, name='business'),
    re_path(r'^(?P<slug>[\w-]+)/detail/$', views.neighborhood_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.hood_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.hood_delete, name='delete'),
    re_path(r'^(?P<slug>[\w-]+)/join/$', views.join_hood, name='join'),
    re_path(r'^(?P<slug>[\w-]+)/leave/$', views.leave_hood, name='leave'),
]