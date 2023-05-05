from django.contrib import admin

from jobs.models import Job

# Register your models here.

class JobsAdmin(admin.ModelAdmin):

    list = ['title', 'organization', 'description',
            'location', 'experience', 'salary', 'work_details', 'job_type']
admin.site.register(Job, JobsAdmin)
