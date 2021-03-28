from django.urls import path
from .views import *
# ProjectCreateView

urlpatterns = [
     #path('home', homePage, name="home"),
     path('', list_Projects, name="home_page"),
     path('login/', LoginPage.as_view(), name="hub_login"),
          path('profile/', profile, name="profile"),
     #path('project/<int:id>', details_project, name="details_project"),
     path('project404/<int:id>', projectDetails, name="details_project_404"),
     # class based
     path('project/', ProjectListView.as_view(), name="project_list"),
     path('project/create', add_project, name="project_create"),
     path('project/delete/<int:id>', delete_project, name="project_delete"),
     path('project/update/<int:id>', update_project, name="project_update"),
     path('project/<int:pk>', ProjectDetailView.as_view(), name="project_detail"),

     # Student
     path('student/', StudentListView.as_view(), name="student_List"),
     path('student/Create', StudentCreateView.as_view(), name="student_Create"),
     path('student/<int:pk>/Update',
          StudentUpdateView.as_view(), name="student_Update"),
     path('student/<int:pk>/Delete',
          StudentDeleteView.as_view(), name="student_Delete"),
     #path('student/create', studentCreate, name="student_create"),
     #path('student/add', studentAdd, name="studentAdd"),
     #path('student/addModel', add_student, name="student_add"),


]
