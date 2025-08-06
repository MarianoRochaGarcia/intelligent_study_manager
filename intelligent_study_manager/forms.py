from django import forms
from accounts.models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'occupation', 'password']
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
            'password' : forms.PasswordInput(attrs={
                'class':"border border-gray-400 rounded-md px-3 py-2 w-full"
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']