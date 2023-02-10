from django.shortcuts import render, redirect, get_object_or_404
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

        context = {
            "users": users
            }
        return render(request, "app_home/developer_overview.html", context)


class ProjectOverview(TemplateView):
    model = Project
    template_name = "app_home/project_overview.html"


class ProfileDetailView(TemplateView):
    model = User
    template_name = "app_home/user_detail_view.html"

    def get(self, request, *args, **kwargs):
        username_for_profile = kwargs["username"]
        user_to_get = get_object_or_404(User, username=username_for_profile)

        context = {
            "user": request.user,
            "user_for_profile": user_to_get
        }
        return render(request, "app_home/user_detail_view.html", context)
