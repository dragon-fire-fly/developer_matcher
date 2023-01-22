from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfilePicture


class UserProfilePictureInLine(admin.TabularInline):
    model = UserProfilePicture
    extra = 0


class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "location",
        "github_user",
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


admin.site.register(User, UserAdmin)

