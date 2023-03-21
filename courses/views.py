from django.shortcuts import render, redirect
from .models import Instructor, Course_Content, Section, Course
from .forms import InstructorForm, Course_ContentForm, SectionForm, CourseForm
# Create your views here.


def add_course_content(request):
    new_course_content = None
    if request.method == "POST":
        form = Course_ContentForm(data=request.POST)

        if form.is_valid():
            new_course_content = form.save(commit=False)
            new_course_content.instructor = request.user.instructor
            new_course_content.save()
            redirect('home')
    else:
        form = Course_ContentForm()

    return render(request, 'courses/add_course_content.html', {'form': form})


def add_section(request):

    if request.method == "POST":
        form = SectionForm(request.POST)

        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.instructor = request.user.instructor
            new_section.save()
            redirect('home')
    else:
        form = SectionForm()

    return render(request, 'courses/add_section.html', {'form': form})


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.post)

        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.instructor = request.user.instructor
            new_course.save()
            redirect('home')

    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})


def learn(request):
    self_paced = Course.objects.filter(type='Self Paced Courses').all()
    live_coherts = Course.objects.filter(type='Live Coherts').all()
    context = {
        'self_paced': self_paced,
        'live_coherts': live_coherts,
    }
    return render(request, 'courses/learn.html', context)


def course_detail(request, id):
    course = Course.objects.filter(id=id).first()
    return render(request, 'courses/course_detail.html', {'course':course})
