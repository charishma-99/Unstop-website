from django.http import HttpResponse
from django.shortcuts import render

def Compete(request):
    return render(request,'compete.html')