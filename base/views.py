from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')


"""Practice Section"""
def practice(request):
    return render(request, 'base/practice.html')