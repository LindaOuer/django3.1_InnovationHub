from django.urls import path
from .views import homePage, list_Projects, details_project, projectDetails, ProjectListView, ProjectDetailView, studentCreate, studentAdd

urlpatterns = [
    #path('home', homePage, name="home"),
    #path('', list_Projects, name="list_projects"),
    #path('project/<int:id>', details_project, name="details_project"),
    path('project404/<int:id>', projectDetails, name="details_project_404"),
    # class based
    path('project/', ProjectListView.as_view(), name="project_list"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name="project_detail"),

    # Student
    path('student/create', studentCreate, name="student_create"),
    path('student/add', studentAdd, name="student_add"),
]
