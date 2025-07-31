from django import forms
from .models import Subject, StudyPlan

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'teacher', 'color', 'description']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'teacher' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'color' : forms.Select(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'description' : forms.Textarea(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full resize-none",
                'rows': 4,
            }),
        }

class StudyPlanForm(forms.ModelForm):
    class Meta:
        model = StudyPlan
        fields = ['title', 'subject', 'start_date', 'limit_date', 'target_hours']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'border border-gray-400 rounded-md px-3 py-2 w-full'
            })
        }


