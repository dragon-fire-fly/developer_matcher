from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserSignupForm


class SignupView(TemplateView):
    model = User
    template_name = "app_user/signup.html"

    def post(self, request, *args, **kwargs):
        signup_form = UserSignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            # automatically log the user in
            login(request, user)
            return redirect(reverse("app_user:success"))
        return redirect(reverse("app_user:signup"))

    def get(self, request, *args, **kwargs):
        signup_form = UserSignupForm

        # show user signup page
        return render(
            request,
            "app_user/signup.html",
            {
                "signup_form": signup_form,
            },
        )
