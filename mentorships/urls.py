from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mentors/', views.mentors, name='mentors'),
    path('add_section', views.add_section, name='add_section'),
    path('add_mentor_content', views.add_mentor_content, name='add_mentor_content'),
    path('add_mentoring_session', views.add_mentoring_session, name='add_mentoring_session'),
    
]