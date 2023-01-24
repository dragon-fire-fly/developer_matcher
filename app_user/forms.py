from django.forms import ModelForm
from .models import User, UserProfilePicture, Project, ProgrammingLanguage


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
