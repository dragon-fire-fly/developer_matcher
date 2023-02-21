from django.urls import path
from . import views

app_name = "app_home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("developers/", views.DeveloperOverview.as_view(), name="developer-overview"),
    path("projects/", views.ProjectOverview.as_view(), name="project-overview"),
    path("projects/create/", views.CreateProjectView.as_view(), name="create-project"),
    path(
        "users/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail-view"
    ),
    path(
        "projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail-view"
    ),
    path(
        "projects/edit/<int:pk>/", views.EditProjectView.as_view(), name="project-edit-view"
    ),
    path(
        "projects/delete/<int:pk>/", views.DeleteProjectView.as_view(), name="delete-project"
    ),
    path(
        "projects/picture/<int:pk>/", views.AddProjectPicture.as_view(), name="add-project-pic"
    ),
]
