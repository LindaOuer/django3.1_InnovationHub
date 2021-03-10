from django import forms

from .models import Project, Student


class StudentForm(forms.Form):
    username = forms.CharField(
        label='Userame',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': 'Enter your username',
            }
        )
    )
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
