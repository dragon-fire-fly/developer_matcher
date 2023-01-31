from django.urls import path
from .views import HomeView, AboutView, DeveloperOverview, ProjectOverview

app_name = "app_home"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("developers/", DeveloperOverview.as_view(), name="developer-overview"),
    path("projects/", ProjectOverview.as_view(), name="project-overview"),
]
