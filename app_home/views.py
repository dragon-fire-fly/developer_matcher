from django.shortcuts import render
from django.views.generic import TemplateView
from app_user.models import User, Project

# Create your views here.


class HomeView(TemplateView):
    model = User
    template_name = "app_home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    model = User
    template_name = "app_home/about.html"


class DeveloperOverview(TemplateView):
    model = User
    template_name = "app_home/developer_overview.html"

    def get(self, request):
        users = User.objects.all()
        context = {"users": users}
        return render(request, "app_home/developer_overview.html", context)


class ProjectOverview(TemplateView):
    model = Project
    template_name = "app_home/project_overview.html"
