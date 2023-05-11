from django import forms
from .models import Section, Mentor, MentorContent, MentoringSession

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('name', 'mentor', 'mentor_content')

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('user', 'profile_photo', 'headline', 'about')

class MentorContentForm(forms.ModelForm):
    class Meta:
        model = MentorContent
        fields = ('mentor', 'name', 'section', 'file')

class MentoringSessionForm(forms.ModelForm):
    class Meta:
        model = MentoringSession
        fields = ('mentor', 'price', 'date', 'location')
        


