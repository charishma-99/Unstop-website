from django.contrib import admin
from .models import Mentor, MentoringSession, MentorContent, Section

# Register your models here.
admin.site.register(Mentor)
admin.site.register(MentoringSession)
admin.site.register(MentorContent)
admin.site.register(Section)