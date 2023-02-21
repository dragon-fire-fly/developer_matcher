from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib import messages
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserRegistrationForm, UserEditForm, AddProfilePictureForm


class RegisterView(TemplateView):
    model = User
    template_name = "app_user/register.html"

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            # automatically log the user in following account creation
            login(request, user)
            return redirect(reverse("app_user:success"))
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )

    def get(self, request, *args, **kwargs):
        # if the user is logged in, registration page is not available
        if request.user.is_authenticated:
            return redirect("/")

        registration_form = UserRegistrationForm
        # show user signup page
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )


class ProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile.html"

    def get(self, request):
        user = request.user
        try:
            user_projects = Project.objects.filter(user=user)
        except:
            user_projects = None
        context = {
            "user": user,
            "user_projects": user_projects,
        }
        return render(request, "app_user/user_profile.html", context)


def delete_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user.delete()
    messages.success(request, "Profile successfully deleted!")
    return redirect(reverse("app_home:index"))


class EditProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        context = {"form": UserEditForm(instance=user)}

        return render(request, "app_user/user_profile_edit.html", context)

    def post(self, request, *args, **kwargs):
        # get the current user (or return a 404)
        user = get_object_or_404(User, pk=request.user.pk)
        # add data to the form and save it
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated!")
        # redirect to main profile page
            return redirect(reverse("app_user:profile"))
        elif "profanity" in form.errors.as_text():
            messages.error(request, "Please do not use profanities in your username!")
            return redirect("app_user:edit-profile")
        elif "duplicate_name" in form.errors.as_text():
            messages.error(request, "Username already in use! Please choose another")
            return redirect("app_user:edit-profile")
        else:
            messages.error(request, "Form could not be submitted")
        return redirect(reverse("app_user:profile"))


class EditProfilePicView(TemplateView):
    model = User
    template_name = "app_user/profile_pic_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        # get all the pictures for the selected user
        pic_query_set = user.profile_pic.values()
        form = AddProfilePictureForm()
        context = {
            "user": user,
            "pictures": pic_query_set,
            "form": form,
        }

        return render(request, "app_user/profile_pic_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        # as there are two post methods (add and delete), they have a hidden input field
        # called "method" added to distinguish them

        # the add route
        if request.POST.get("method") == "add":
            new_picture = AddProfilePictureForm(
                request.POST, request.FILES, initial={"user": user}
            )
            if new_picture.is_valid():
                new_picture = new_picture.save(commit=False)
                new_picture.user = user
                new_picture.save()
            return redirect(reverse("app_user:edit-profile-pic"))

        # the delete route
        elif request.POST.get("method") == "delete":
            # retrieve the id from the post request in the template
            pic_id = int(request.POST["pic_id"])
            picture = get_object_or_404(UserProfilePicture, pk=pic_id)
            picture.delete()
        return redirect(reverse("app_user:edit-profile-pic"))
