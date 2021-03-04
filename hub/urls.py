from django.urls import path
from .views import homePage, list_Projects, details_project

urlpatterns = [
    path('home', homePage, name="home"),
    path('', list_Projects, name="list_projects"),    
    path('project/<int:id>', details_project, name="details_project"),    
]