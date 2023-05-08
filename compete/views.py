from django.shortcuts import render

# Create your views here.
def compete_portal(request):
    return render(request,'compete.html')
