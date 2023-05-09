from django.shortcuts import render


def jobs(request):
    return render(request, 'job-main.html')