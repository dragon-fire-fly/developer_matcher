from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django_countries.fields import CountryField
from .models import User, ProgrammingLanguage, UserProfilePicture


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Enter a valid email address", required=True)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    p_language_queryset = ProgrammingLanguage.objects.all()
    p_language_choices = []
    for language in p_language_queryset:
        p_language_choices.append((language.id, language.language))
    p_language = forms.MultipleChoiceField(
        choices=p_language_choices, widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "p_language",
            "location",
            "github_username",
            "github_url",
            "linked_in",
            "portfolio",
        ]


class AddProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfilePicture
        fields = "__all__"
        exclude = ["user"]
