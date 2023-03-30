from django.db import models
from accounts.models import UserProfile
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.


def create_slug(title):
    slug = slugify(title)
    qs = Course.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug, qs.first().id)
    return slug

class Instructor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    headline = models.CharField(max_length=150)
    about = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.headline}"


class Course_Content(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    file = models.FileField(upload_to='course_content/')

    def __str__(self):
        return f"{self.name} - {self.section} | {self.course}"


class Section(models.Model):
    instructor = models.ManyToManyField(Instructor)
    name = models.CharField(max_length=255)
    course_content = models.ManyToManyField(
        Course_Content, related_name="course_contents")
    course = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.course}"


class Course(models.Model):
    COURSE_TYPE = (
        ('Self Paced Courses', 'Self Paced Courses'),
        ('Live Coherts', 'Live Coherts'),
    )
    course_cover = models.ImageField( upload_to='course_cover/', blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    type = models.CharField(max_length=20, choices=COURSE_TYPE)
    langauge = models.CharField(max_length=255)
    intro_video = models.FileField(upload_to='intro_video/')
    about = models.TextField()
    duration = models.CharField( max_length=50)
    course_highlight = models.TextField()
    section = models.ManyToManyField(Section, related_name="sections")
    price = models.FloatField(default=0)
    career_growth_prospect = models.TextField()
    instructor = models.ManyToManyField(Instructor, related_name="instructors")
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        return super().save(*args, **kwargs)
