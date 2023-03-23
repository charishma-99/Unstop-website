from django.urls import path
from . import views

urlpatterns = [
    path('job-portal/',views.job_portal,name='job_portal'),
]
