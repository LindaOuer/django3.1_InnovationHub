from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project, Student
from .forms import StudentForm, StudentModelForm, ProjectForm, CustomUserCreationForm


# function based views
def homePage(request):
    return HttpResponse('<h1>Welcome To ... </h1>')


def list_Projects(request):
    list = Project.objects.all()
    return render(
        request,
        'hub/index.html',
        {
            'projects': list,
        },
    )


@login_required
def details_project(request, id):
    project = Project.objects.get(pk=id)
    return render(
        request,
        'hub/details_project.html',
        {
            'project': project,
        }
    )


@login_required
def projectDetails(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(
        request,
        'hub/details_project.html',
        {
            'project': project
        }
    )


def studentCreate(request):
    # print(request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        Student.objects.create(
            first_name=first_name, last_name=last_name, email=email, username=username)

        return redirect("project_list")

    return render(request, 'hub/student_create.html', )


def studentAdd(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # print(form.cleaned_data.get('username'))
            # Student.objects.create(**form.cleaned_data)

            Student.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data.get('username'))
        # else:
        #    print(form.errors)

    return render(request, 'hub/student_add.html', {'form': form})


def add_student(request):
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, 'hub/student_add.html', {'form': form})
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            postStudent = form.save(commit=False)
            postStudent.save()
            return redirect('project_list')
        else:
            return render(request, 'hub/student_add.html',
                          {'msg_error': "Error when adding a student", 'form': form})


def add_project(request):
    if request.method == "GET":
        form = ProjectForm()
        return render(request, 'hub/project_form.html', {'form': form})
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            print((form.cleaned_data.get('members')))
            form.save()
            return redirect('project_list')
        else:
            return render(request, 'hub/project_form.html',
                          {'msg_error': "Error when adding a project", 'form': form})


def delete_project(request, id):
    #project = Project.objects.get(pk=id)
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('project_list')


def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')

    return render(request, 'hub/project_form.html', {'form': form, 'id': id})

# class based views


class ProjectListView(ListView):
    model = Project
    #template_name = "hub\project_list.html"


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


"""class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
"""

# Student Model


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    #template_name = "hub\student_form.html"


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    #template_name = "hub\student_form.html"


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_List')


# Login - Logout

class LoginPage(LoginView):
    template_name = "hub\login.html"
    fields = '__all__'
    redirect_authentcated_user = True

    def get_success_url(self):
        return reverse_lazy("project_create")


@login_required
def profile(request):
    return render(request, 'hub/profile.html')


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request, f'The account of {username} was successfully created')
                return redirect('home_page')
            else:
                messages.warning(
                    request, f'Something went wrong, please try to login')
                return redirect('login')

    return render(request, "hub/register.html", {'form': form})
