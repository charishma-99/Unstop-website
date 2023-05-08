from django.shortcuts import render

# Create your views here.
def job_portal(request):
    return render(request,'job-main.html')