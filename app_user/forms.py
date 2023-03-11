from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ValidationError
from django_countries.fields import CountryField
from better_profanity import profanity
from .models import User, ProgramLang, UserProfilePicture, Message


def validate_username(data):
    """Checks that a username is not already taken and does not
    contain profanities"""

    if isinstance(data, str):
        username = data
    else:
        username = data.cleaned_data["username"]
        if data.instance:
            # check if username is unchanged
            if data.instance.username == username:
                return

    # Check username for profanity and do not allow if present
    if profanity.contains_profanity(username):
        raise ValidationError("profanity")
    else:
        # Check if username already taken and return error if so
        try:
            taken_username = User.objects.get(username=username)
            raise ValidationError("duplicate_name")
        except User.DoesNotExist:
            return


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Enter a valid email address", required=True
    )

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
    # p_language_objects = ProgramLang.objects.all()
    # lang_choices = []
    # for lang in p_language_objects:
    #     lang_choices.append((lang.id, lang.language))
    # p_language = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(), choices=lang_choices
    # )

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
        labels = {
            "p_language": "Programming Language(s)",
        }

    # def __init__(self, *args, **kwargs):
    #     super(UserEditForm, self).__init__(*args, **kwargs)
    #     p_lang_q_set = ProgramLang.objects.filter(user=self.instance)
    #     p_langs_init = []
    #     for lang in p_lang_q_set:
    #         p_langs_init.append(lang.pk)
    #     self.initial["p_language"] = p_langs_init

    def clean(self):
        validate_username(self)


class AddProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfilePicture
        fields = "__all__"
        exclude = ["user"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "message"]

    def save(self, msgtype, commit=True):
        message = super(MessageForm, self).save(commit=False)
        if msgtype == "edit":
            message.edited = True
        if commit:
            message.save()
        return message
