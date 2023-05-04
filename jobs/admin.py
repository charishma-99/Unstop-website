from django.contrib import admin
from jobs.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list = ['title', 'organization', 'description', 'application_deadline', 'location', 'experience', 'salary', 'work_details', 'job_type']

admin.site.register(Job, JobAdmin)