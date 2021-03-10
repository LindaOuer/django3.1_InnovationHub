from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView

from .models import Project, Student
from .forms import StudentForm


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


def details_project(request, id):
    project = Project.objects.get(pk=id)
    return render(
        request,
        'hub/details_project.html',
        {
            'project': project,
        }
    )


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
            #print(form.cleaned_data)
            #print(form.cleaned_data.get('username'))
            # Student.objects.create(**form.cleaned_data)
            
            Student.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data.get('username'))
        # else:
        #    print(form.errors)

    return render(request, 'hub/student_add.html', {'form': form})

# class based views


class ProjectListView(ListView):
    model = Project
    #template_name = "hub\project_list.html"


class ProjectDetailView(DetailView):
    model = Project
