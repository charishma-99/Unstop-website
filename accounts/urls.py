from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerpage, name='register'),
 
]
