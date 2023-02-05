from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView, ProfileView, EditProfileView

app_name = "app_user"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", EditProfileView.as_view(), name="edit-profile"),
    path(
        "success/",
        TemplateView.as_view(template_name="app_user/success.html"),
        name="success",
    ),
]
