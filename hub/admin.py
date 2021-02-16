from django.contrib import admin
from .models import Student, Coach, User, Project

# Register your models here.


class ProjectInline(admin.TabularInline):
    model = Project
    fieldsets = [
        (
            None,
            {
                'fields': ['project_name']
            }
        )
    ]
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'email'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    inlines = [
        ProjectInline
    ]

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
    )
    fields = (
        (
            'last_name',
            'first_name',
        ),
        'email'
    )
admin.site.register(Student, StudentAdmin)

admin.site.register(User)

admin.site.register(Project)
