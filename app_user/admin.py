from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfilePicture, Project, ProgrammingLanguage


class UserProfilePictureInLine(admin.TabularInline):
    model = UserProfilePicture
    extra = 0


class ProjectInLine(admin.TabularInline):
    model = Project
    extra = 0


class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "p_language",
        "location",
        "github_username",
        "github_url",
        "linked_in",
        "portfolio",
        "date_joined",
        "last_login",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    inlines = [UserProfilePictureInLine]


class ProjectAdmin(admin.ModelAdmin):
    fields = ["title", "description", "user"]


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    fields = ["language"]


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
