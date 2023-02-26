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
    path("messages/", views.Messages.as_view(), name="messages"),
    path("messages/<int:pk>/", views.IndividualMsg.as_view(), name="individual_msg"),
    path("messages/send/<int:pk>/", views.AddMessage.as_view(), name="add_message"),
    path(
        "messages/delete/<int:pk>/",
        views.DeleteMessage.as_view(),
        name="delete_message",
    ),
]
