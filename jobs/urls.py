from django.urls import path
from . import views

urlpatterns = [
    path('',views.job_portal,name='job_portal'),
]
