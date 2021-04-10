from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('hoods', views.hood, name="hoods"),
    path('create', views.new_hood, name='create'),
    path('profile', user_profile, name='profile'),

]