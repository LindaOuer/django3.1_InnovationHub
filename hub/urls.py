from django.urls import path
from .views import homePage, list_Projects

urlpatterns = [
    path('home', homePage, name="home"),
    path('', list_Projects, name="list_projects")
]