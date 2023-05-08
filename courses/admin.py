from django.contrib import admin
from .models import Instructor, Course_Content, Section, Course

# Register your models here.

admin.site.register(Instructor)
admin.site.register(Course_Content)
admin.site.register(Section)
admin.site.register(Course)
