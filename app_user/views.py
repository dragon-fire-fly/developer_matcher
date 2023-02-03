from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserRegistrationForm, UserEditForm


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
        user = get_object_or_404(User, pk=request.user.pk)
        return redirect(reverse("app_user:edit-profile"))


class EditProfileView(TemplateView):
    model = User
    template_name = "app_user/user_profile_edit.html"

    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)

        context = {"form": UserEditForm(instance=user)}

        return render(request, "app_user/user_profile_edit.html", context)
