from django.shortcuts import render
from .models import Mentor
from accounts.views import ShowProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mentors(request):
    mentors = Mentor.objects.all()
    context = {
        'mentors': mentors,
    
    }
    return render(request, 'mentors.html', context)