from django import forms
from my_course.models import Course


class CourseForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required = False)
    class Meta:
        model = Course
        exclude = ["is_done"]