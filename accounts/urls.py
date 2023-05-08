from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerpage, name='register'),
    path('<int:pk>/profile', views.ShowProfile.as_view(), name='profile_page'),
 
]
