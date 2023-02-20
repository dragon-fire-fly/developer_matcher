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
        "users/<str:username>/", views.ProfileDetailView.as_view(), name="profile-detail-view"
    ),
    path(
        "projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail-view"
    ),
    path(
        "projects/edit/<int:pk>/", views.ProjectEditView.as_view(), name="project-edit-view"
    ),
]
