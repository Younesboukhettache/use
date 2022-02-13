from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [path('', views.younes, name='home'),
path('new/', views.new, name='new'),
path('enter/', views.dkhal, name='enter'),
path('logout/', views.out, name='out'),
path('share/', views.post, name='post'),



]
