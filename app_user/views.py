from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import User, UserProfilePicture, Project, ProgrammingLanguage
from .forms import UserSignupForm


class SignupView(FormView):
    # model = User
    template_name = "app_user/signup.html"
    form_class = UserSignupForm
