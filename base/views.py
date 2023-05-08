from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html')


"""Practice Section"""
def practice(request):
    return render(request, 'base/practice.html')
def compete(request):
    return render(request,'compete/compete.html')
def job(request):
    return render(request,'jobs/job-main.html')
def mentors(request):
    return render(request,'mentorships/home.html')