from django.shortcuts import render, redirect
from .models import Mentor, MentoringSession, MentorContent, Section
from .forms import SectionForm, MentorContentForm, MentoringSessionForm
from accounts.views import ShowProfile

# Create your views here.
def home(request):
    return render(request, 'mentorships/home.html')

def beamentor(request):
    return render(request, 'mentorships/add_section.html')

def form(request):
    return render(request, 'mentorships/form.html')

def mentors(request):
    mentors = Mentor.objects.all()
    id = request.GET.get('id')
    if id == '1':
        mentors = Mentor.objects.filter(mentor_type='technology')
    elif id == '2':
        mentors = Mentor.objects.filter(mentor_type='management')
    elif id == '3':
        mentors = Mentor.objects.all()
    else:
        mentors = Mentor.objects.all()

    # technology_mentors = Mentor.objects.filter(mentor_type='Technology').all()
    # management_mentors = Mentor.objects.filter(mentor_type='Management').all()
    context = {
        'mentors': mentors,
        # 'technology_mentors': technology_mentors,
        # 'management_mentors': management_mentors,

    }
    return render(request, 'mentorships/mentors.html', context)

def add_section(request):
    
    if request.method == "POST":
        form = SectionForm(request.POST)

        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.mentor = request.user.mentor
            new_section.save()
            redirect('home')
    
    else:
        form = SectionForm()
   
    return render(request, 'mentorships/add_section.html', {"form": form})

def add_mentor_content(request):
    new_mentor_content = None
    if request.method == 'POST':
        form = MentorContentForm()
        if form.is_valid:
            new_mentor_content = form.save()
            new_mentor_content.mentor = request.user.mentor
            new_mentor_content.save()
            redirect('home')

    else:
        form = MentorContentForm()

    return render(request, 'mentorships/mentor_content.html', {'form': form})

def add_mentoring_session(request):
    new_mentoring_session = None
    if request.method == 'POST':
        form = MentoringSessionForm()
        if form.is_valid:
            new_mentoring_session = form.save()
            new_mentoring_session.mentor = request.user.mentor
            new_mentoring_session.save()
            redirect('home')

    else:
        form = MentoringSessionForm()

    return render(request, 'mentorships/mentoring_session.html', {'form': form})

