from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserSignupForm


class RegisterView(TemplateView):
    model = User
    template_name = "app_user/register.html"

    def post(self, request, *args, **kwargs):
        registration_form = UserSignupForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            # automatically log the user in
            login(request, user)
            return redirect(reverse("app_user:success"))
        return redirect(reverse("app_user:register"))

    def get(self, request, *args, **kwargs):
        registration_form = UserSignupForm

        # show user signup page
        return render(
            request,
            "app_user/register.html",
            {
                "registration_form": registration_form,
            },
        )
