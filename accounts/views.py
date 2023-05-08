from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserSignupForm
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile, Profile
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def registerpage(request):
    form = UserSignupForm()
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def home(request):
    return render(request, 'registration/home.html')


class ShowProfile(generic.DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfile, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context

