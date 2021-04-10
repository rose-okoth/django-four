from . import views
from django.urls import path, re_path

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('hoods', views.hood, name="hoods"),
    path('create', views.new_hood, name='create'),
    path('profile', views.user_profile, name='profile'),
    re_path(r'^(?P<slug>[\w-]+)/post/$', views.create_post, name='post'),
    re_path(r'^(?P<slug>[\w-]+)/detail/$', views.neighborhood_detail, name='detail'),

]