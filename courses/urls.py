from django.urls import path
from . import views

urlpatterns = [
    path('add-course-content/', views.add_course_content, name="add_course_content"),
    path('add-section/', views.add_section, name="add_section"),
    path('add-course/', views.add_course, name="add_course"),
    path('', views.learn, name="learn"),
    path('detail/<slug:slug>', views.course_detail, name="course_detail"),
]
