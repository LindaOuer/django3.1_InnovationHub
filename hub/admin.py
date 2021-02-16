from django.contrib import admin
from .models import Student, Coach, User, Project, MembershipInProject

# Register your models here.

admin.site.register(User)


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


admin.site.register(Student, StudentAdmin)


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


class MembershipInline (admin.StackedInline):
    model = MembershipInProject
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'created_at',
        'updated_at',
        'project_duration',
        'creator',
        'supervisor'
    )
    
    date_hierarchy = 'updated_at'

    fieldsets = (
        (
            'Etat',
            {
                'fields': ('isValid',)
            }
        ),
        (
            'A Propos',
            {
                'classes': ('collapse',),
                'fields': (
                    'project_name',
                    (
                        'creator',
                        'supervisor',
                    ),
                    'needs',
                    'description',
                ),
            }
        ),
        (
            'Durées',
            {
                'fields': (
                    (
                        'project_duration',
                        'time_allocated'
                    ),
                )
            }
        ),
    )
    inlines = [MembershipInline]
    empty_value_display = '-empty-'


admin.site.register(Project, ProjectAdmin)
