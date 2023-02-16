from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "app_user"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.EditProfileView.as_view(), name="edit-profile"),
    path("profile/delete/", views.delete_profile, name="delete-profile"),
    path(
        "profile/picture/", views.EditProfilePicView.as_view(), name="edit-profile-pic"
    ),
    path(
        "success/",
        TemplateView.as_view(template_name="app_user/success.html"),
        name="success",
    ),
]
