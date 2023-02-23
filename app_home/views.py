from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, FormView
from app_user.models import User, Project, ProgrammingLanguage, ProjectPicture
from .forms import ProjectCreationForm, ProjectEditForm, AddProjectPictureForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(TemplateView):
    """
    View for the home page.
    """

    model = User
    template_name = "app_home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    """
    View for the about page.
    """

    model = User
    template_name = "app_home/about.html"


class DeveloperOverview(TemplateView, LoginRequiredMixin):
    """
    View for the general overview displaying all users except the logged in user.
    """

    model = User
    template_name = "app_home/developer_overview.html"

    def get(self, request):
        users = User.objects.all()

        context = {"users": users}
        return render(request, "app_home/developer_overview.html", context)


class ProfileDetailView(TemplateView):
    """
    View for rendering detailed profile view for chosen user.
    """

    model = User
    template_name = "app_home/user_detail_view.html"

    def get(self, request, *args, **kwargs):
        profile_pk = kwargs["pk"]
        user_to_get = get_object_or_404(User, pk=profile_pk)
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
    """
    Project overview view.
    """

    model = Project
    template_name = "app_home/project_overview.html"

    def get(self, request):
        projects = Project.objects.all()

        context = {"projects": projects}
        return render(request, "app_home/project_overview.html", context)


class ProjectDetailView(TemplateView):
    """
    View for rendering the detail page for a project.
    """

    model = Project
    template_name = "app_home/project_detail_view.html"

    def get(self, request, *args, **kwargs):
        project_pk = kwargs["pk"]
        project_to_get = get_object_or_404(Project, pk=project_pk)

        context = {"user": request.user, "project": project_to_get}

        return render(request, "app_home/project_detail_view.html", context)


class CreateProjectView(FormView):
    """
    View to create a project.
    """

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
            return redirect(
                reverse("app_home:project-detail-view", kwargs={"pk": new_project.pk})
            )
        elif "profanity" in form.errors.as_text():
            messages.error(
                request, "Please do not use profanities in your project name!"
            )
        elif "duplicate_name" in form.errors.as_text():
            messages.error(
                request, "Project name already taken! Please choose another."
            )
        else:
            messages.error(request, "Please select at least one programming language")
        return redirect(reverse("app_home:create-project"))


class EditProjectView(TemplateView):
    """
    View to edit a project
    """

    model = Project
    template_name = "app_home/edit_project.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        context = {"form": ProjectEditForm(instance=project)}

        return render(request, "app_home/edit_project.html", context)

    def post(self, request, *args, **kwargs):
        user = request.user
        project = get_object_or_404(Project, pk=kwargs["pk"])
        form = ProjectEditForm(request.POST, instance=project)
        p_langs = form.data.getlist("p_language")
        if form.is_valid():
            project = form.save(commit=False)
            project.p_language.set(p_langs)
            project.save()
            messages.success(request, "Project successfully edited!")
            return redirect(
                reverse("app_home:project-detail-view", kwargs={"pk": project.pk})
            )
        elif "profanity" in form.errors.as_text():
            messages.error(
                request, "Please do not use profanities in your project name!"
            )
            return render(request, "app_home/edit_project.html", {"form": form})
        elif "duplicate_name" in form.errors.as_text():
            messages.error(
                request, "Project name already in use! Please choose another"
            )
            return render(request, "app_home/edit_project.html", {"form": form})
        elif not form["p_language"].value():
            messages.error(request, "Please select at least one programming language")
        else:
            messages.error(request, "Form could not be submitted. Please try again")
        return render(request, "app_home/edit_project.html", {"form": form})


class DeleteProjectView(TemplateView):
    """
    View to delete a project
    """

    model = Project
    template_name = "app_home/about.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        project.delete()
        messages.success(request, "Profile successfully deleted!")
        return redirect(reverse("app_home:project-overview"))


class AddProjectPicture(TemplateView):
    """
    View to add a picture to a project
    """

    model = ProjectPicture
    template_name = "app_home/project_picture.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        if project.project_pic:
            pic_query_set = project.project_pic.values()
        else:
            pic_query_set = [""]
        form = AddProjectPictureForm()
        context = {
            "project": project,
            "pictures": pic_query_set,
            "form": form,
        }
        return render(request, "app_home/project_picture.html", context)

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        project_pk = project.pk

        new_picture = AddProjectPictureForm(
            request.POST, request.FILES, initial={"project": project}
        )
        if new_picture.is_valid():
            new_picture = new_picture.save(commit=False)
            new_picture.project = project
            new_picture.save()

        return redirect(
            reverse("app_home:project-detail-view", kwargs={"pk": project_pk})
        )


class DeleteProjectPicture(TemplateView):
    """
    View to delete pictures from projects
    """

    model = ProjectPicture
    template_name = "app_home/project_picture.html"

    def get(self, request, *args, **kwargs):
        pic_to_delete = get_object_or_404(ProjectPicture, pk=kwargs["pk"])
        pic_to_delete.delete()
        return redirect(reverse("app_home:project-overview"))
