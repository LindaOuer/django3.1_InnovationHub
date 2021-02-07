from django.contrib import admin
from .models import Student, Coach, User, Project

# Register your models here.

admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Student)
admin.site.register(Project)
