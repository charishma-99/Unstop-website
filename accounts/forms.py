from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields= ('email','first_name', 'last_name', 'username', 'gender', 'phone', 'organization', 'password1', 'password2')