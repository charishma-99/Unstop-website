from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('practice/', views.practice, name="practice"),
    path('compete/',views.compete,name='compete'),
    path('job/',views.job,name='job_portal'),
    path('mentors/',views.mentors,name = 'mentorship')

]
