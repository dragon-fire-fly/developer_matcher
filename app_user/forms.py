from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ValidationError
from django_countries.fields import CountryField
from better_profanity import profanity
from .models import User, ProgrammingLanguage, UserProfilePicture


def validate_username(data):
    """Checks that a username is not already taken and does not
    contain profanities"""

    if isinstance(data, str):
        username = data
    else:
        username = data.cleaned_data["username"]

    # Check username for profanity and do not allow if present
    if profanity.contains_profanity(username):
        raise ValidationError(
            "Please do not use profanities in your username!"
        )
    else:
        # Check if username already taken and return error if so
        try:
            taken_username = User.objects.get(username=username)
            raise ValidationError(
                "The chosen username is already taken. Please choose another.",
                code="invalid")
        except User.DoesNotExist:
            return


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

    def clean(self):
        validate_username(self)


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
