from django.db import models

# Create your models here.

class Organization(models.Model):
    cover_image = models.ImageField(upload_to='organization_cover_images/')
    name = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance')
    ]
    title = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='jobs')
    description = models.TextField()
    application_deadline = models.DateTimeField()
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    work_details = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)

    def __str__(self):
        return self.title