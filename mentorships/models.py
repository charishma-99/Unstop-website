from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Mentor(models.Model):
    MENTOR_TYPE = [
        # ('technology', 'Technology'),
        # ('management', 'Management'),
        {id: '1', type: 'technology'},
        {id: '2', type: 'management'},
    ]
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    headline = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    expertise = models.CharField(max_length=500)
    mentoring_style = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    education = models.CharField(max_length=150)
    work_experience = models.CharField(max_length=500)
    mentor_type = models.CharField(max_length=100, choices=MENTOR_TYPE, null=True)

    def __str__(self):
        return f"{self.profile_photo} -{self.headline}"

# class Mentee(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
#     about = models.TextField()
#     areas_of_interest = models.CharField(max_length=300)
#     preffered_mentoring_style = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.name} - {self.about}"
        

class MentoringSession(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    
    price = models.FloatField(default=0)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.mentor} - {self.price} - {self.date}"

class MentorContent(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    mentor = models.CharField(max_length=250)
    file = models.FileField(upload_to='mentorcontent')

    def __str__(self):
        return f"{self.name} - {self.section} - {self.mentor}"


class Section(models.Model):
    mentor = models.ManyToManyField(Mentor)
    name = models.CharField(max_length=150)
    mentor_content = models.ManyToManyField(MentorContent, related_name="mentorcontent")

        




