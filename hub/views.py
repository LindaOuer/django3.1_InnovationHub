from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Project


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


# class based views
class ProjectListView(ListView):
    model = Project
    #template_name = "hub\project_list.html"
