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

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__' # all fields from AbstractUser even groups and user permessions 
        fields = ['username', 'first_name', 'last_name' ,'email']
        # exclude = ['email']
        help_texts = {
            'last_name': 'Your name here!',
        }
        error_messages = {
            'last_name': {
                'max_length': "This student's name is too long.",
            },

        }