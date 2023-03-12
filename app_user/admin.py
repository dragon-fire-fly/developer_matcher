from django.contrib import admin

from .models import (
    User,
    UserProfilePicture,
    Project,
    ProjectPicture,
    ProgramLang,
    Message,
)


class UserProfilePictureInLine(admin.TabularInline):
    model = UserProfilePicture
    extra = 0


class ProjectPictureInLine(admin.TabularInline):
    model = ProjectPicture
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
    fields = ["title", "description", "user", "p_language"]
    inlines = [ProjectPictureInLine]


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    fields = ["language", "language_icon"]


class MessageAdmin(admin.ModelAdmin):
    fields = ["user_sender", "user_receiver", "title", "message", "edited"]
    exclude = ["sent_date"]


# Register User,Project and ProgrammingLanguage
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProgramLang, ProgrammingLanguageAdmin)
admin.site.register(Message, MessageAdmin)
