from django import forms
from .models import Subject, StudyPlan, StudySession

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
            }),
            'subject' : forms.Select(attrs={
                'class' : 'border border-gray-400 rounded-md px-3 py-2 w-full'
            }),
            'start_date' : forms.TimeInput(attrs={
                "type": 'date',
                'class' : 'border border-gray-400 rounded-md px-3 py-2 w-full',
                },
                format='%Y-%m-%d'
            ),
            'limit_date' : forms.TimeInput(attrs={
                "type": 'date',
                'class' : 'border border-gray-400 rounded-md px-3 py-2 w-full',
                },
                format='%Y-%m-%d'
            ),
            'target_hours' : forms.TextInput(attrs={
                'class' : 'border border-gray-400 rounded-md px-3 py-2 w-full'
            }),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['title', 'study_plan', 'start', 'end', 'notes']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'study_plan' : forms.Select(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'start' : forms.TimeInput(attrs={
                "type": 'datetime-local',
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full",
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'end' : forms.TimeInput(attrs={
                "type": 'datetime-local',
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full",
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'notes' : forms.Textarea(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full resize-none",
                'rows': 4,
            }),
        }
