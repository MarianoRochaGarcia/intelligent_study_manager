from django import forms
from.models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'occupation']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'email' : forms.EmailInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'first_name' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
            'last_name' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full resize-none"
            }),
            'occupation' : forms.TextInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full resize-none"
            }),
        }

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']