from django import forms
from my_course.models import Course

"""
HTML Integrated form with excluded fields. Hidden from mentor to register and id and student hidden from Django Table.
"""

class CourseForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required = False)
    enroll_now = forms.BooleanField(widget=forms.HiddenInput, required = False)
    class Meta:
        model = Course
        exclude = ["id", "students"]