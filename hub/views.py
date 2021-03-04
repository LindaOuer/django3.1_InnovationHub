from django.shortcuts import render
from django.http import HttpResponse

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