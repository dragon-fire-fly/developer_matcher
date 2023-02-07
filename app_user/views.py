from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
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
        return redirect(reverse("app_user:register"))

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        if request.POST["method"] == "edit":
            return redirect(reverse("app_user:edit-profile"))
        elif request.POST["method"] == "delete":
            print("delete!")
            user = get_object_or_404(User, pk=request.user.pk)
            user.delete()
            return redirect(reverse("app_user:register"))
        return redirect(reverse("app_user:profile"))


class EditProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        context = {"form": UserEditForm(instance=user)}

        return render(request, "app_user/user_profile_edit.html", context)

    def post(self, request):
        # get the current user (or return a 404)
        user = get_object_or_404(User, pk=request.user.pk)
        # add data to the form and save it
        form = UserEditForm(request.POST, instance=user)
        form.save()
        # redirect to main profile page
        return redirect(reverse("app_user:profile"))


class EditProfilePicView(TemplateView):
    model = User
    template_name = "app_user/profile_pic_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        pictures = []
        for picture in user.profile_pic.values():
            pictures.append(picture["profile_picture"].url)
        context = {
            "user": user,
            "pictures": pictures
        }

        return render(request, "app_user/profile_pic_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        if request.POST.get("method") == "add":
            new_picture = AddProfilePictureForm(
                request.POST,
                request.FILES,
                initial={"user": user}
            )
            if new_picture.is_valid():
                new_picture = new_picture.save(commit=False)
                new_picture.user = user
                new_picture.save()
            return redirect(reverse("app_user:edit-profile-pic"))

        elif request.POST.get("method") == "delete":
            print("delete")
        return redirect(reverse("app_home:about"))
