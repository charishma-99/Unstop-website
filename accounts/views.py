from django.shortcuts import render
from .forms import UserSignupForm
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserSignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def home(request):
    return render(request, 'registration/home.html')