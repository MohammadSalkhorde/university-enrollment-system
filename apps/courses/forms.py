from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'capacity', 'professor', 'prerequisites', 'day', 'start_time', 'end_time', 'location']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input-field'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input-field'}),
            'prerequisites': forms.SelectMultiple(attrs={'class': 'input-field'}),
        }