# Generated by Django 4.1 on 2023-03-20 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('section', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='course_content/')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('course_content', models.ManyToManyField(related_name='course_contents', to='courses.course_content')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('headline', models.CharField(max_length=150)),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('langauge', models.CharField(max_length=255)),
                ('intro_video', models.FileField(upload_to='intro_video/')),
                ('about', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('course_highlight', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('career_grouth_prospect', models.TextField()),
                ('instructor', models.ManyToManyField(related_name='instructors', to='courses.instructor')),
                ('section', models.ManyToManyField(related_name='sections', to='courses.section')),
            ],
        ),
    ]