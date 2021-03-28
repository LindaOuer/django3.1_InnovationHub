from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Project, Student, MembershipInProject, User


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
        fields = ['username', 'first_name', 'last_name', 'email']
        # exclude = ['email']
        help_texts = {
            'last_name': 'Your name here!',
        }
        error_messages = {
            'last_name': {
                'max_length': "This student's name is too long.",
            },

        }


class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    time_allocated_by_member = forms.IntegerField()

    class Meta:
        model = Project
        fields = '__all__'
        #exclude = ['members', ]

    def save(self, commit=True):

        # Save the project so we have an ID for the m2m
        project = super(ProjectForm, self).save()
        print(self.cleaned_data)

        time_allocated_by_member = self.cleaned_data.get(
            'time_allocated_by_member')
        print(time_allocated_by_member)
        """time_allocated_by_member = Project.objects.get(time_allocated_by_member=time_allocated_by_member)
        """

        MembershipInProject.objects.update(
            time_allocated_by_member=time_allocated_by_member)

        return project


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')