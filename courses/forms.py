from django import forms
from .models import Instructor, Course_Content, Section, Course


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ('__all__')


class Course_ContentForm(forms.ModelForm):
    class Meta:
        model = Course_Content
        fields = ('__all__')


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('__all__')


class CourseForm(forms.Modelform):
    class Meta:
        model = Course
        fields = ('name', 'type', 'language',
                  'intro_video', 'about', 'duration', 'course_heightlight', 'section', 'price', 'career_growth_prospect', 'instructor')