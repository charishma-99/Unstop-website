from django.shortcuts import render


def job_portal(request):
    return render(request, 'job-main.html')