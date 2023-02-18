from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, FormView
from app_user.models import User, Project, ProgrammingLanguage
from .forms import ProjectCreationForm
from django.contrib import messages

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


class ProfileDetailView(TemplateView):
    model = User
    template_name = "app_home/user_detail_view.html"

    def get(self, request, *args, **kwargs):
        username_for_profile = kwargs["username"]
        user_to_get = get_object_or_404(User, username=username_for_profile)
        try:
            user_to_get_projects = Project.objects.filter(user=user_to_get)
        except:
            user_to_get_projects = None
        context = {
            "user": request.user,
            "user_for_profile": user_to_get,
            "user_projects": user_to_get_projects,
        }
        return render(request, "app_home/user_detail_view.html", context)


class ProjectOverview(TemplateView):
    model = Project
    template_name = "app_home/project_overview.html"

    def get(self, request):
        projects = Project.objects.all()

        context = {"projects": projects}
        return render(request, "app_home/project_overview.html", context)


class ProjectDetailView(TemplateView):
    model = Project
    template_name = "app_home/project_detail_view.html"

    def get(self, request, *args, **kwargs):
        project_for_profile = kwargs["title"]
        project_to_get = get_object_or_404(Project, title=project_for_profile)

        context = {"user": request.user, "project": project_to_get}

        return render(request, "app_home/project_detail_view.html", context)


class CreateProjectView(FormView):
    template_name = "app_home/create_project.html"
    form_class = ProjectCreationForm

    def get(self, request):
        project_form = ProjectCreationForm()
        context = {"form": project_form}

        return render(request, "app_home/create_project.html", context)

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST)
        p_langs = form.data.getlist("p_language")

        if form.is_valid():
            new_project = form.save()
            new_project.user.add(user)
            for lang in p_langs:
                new_project.p_language.add(lang)
                new_project.save()
            messages.success(request, "Project successfully created!")
            return redirect(reverse("app_home:project-overview"))
        messages.error(request, "Project not created")
        return redirect(reverse("app_home:create-project"))
