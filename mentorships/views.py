from django.shortcuts import render
from .models import Mentor
from accounts.views import ShowProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mentors(request):
    mentors = Mentor.objects.all()
    id= request.GET.get('id')
    if id=='1':
        mentors = Mentor.objects.filter(mentor_type= 'technology')
    elif id=='2':
        mentors = Mentor.objects.filter(mentor_type= 'management')
    elif id=='3':
        mentors = Mentor.objects.all() 
    else:
      mentors = Mentor.objects.all()  
    context = {
        'mentors': mentors,
    }
    return render(request, 'mentors.html', context)