from django.urls import path
from . import views

urlpatterns = [
    path('',views.compete_portal,name='compete_portal'),
]