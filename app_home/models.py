from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField

PROGRAMMING_LANGUAGES = [
    ("python", "Python"),
    ("html", "HTML"),
    ("css", "CSS"),
    ("javascript", "Javascript")
    ]


class User(AbstractUser):
    '''Inherits from AbstractUser to gain username, email, first_name,
    last_name and date_joined fields.
    Adds additional specific fields to this model.
    '''
    p_language = MultiSelectField(
        max_length=50,
        help_text="Choose your programming language(s)",
        choices=PROGRAMMING_LANGUAGES
        )
    location = models.CharField(
        help_text="Where do you live?",
        max_length=255, blank=True, null=True
        )
    github_username = models.CharField(
        help_text="What is your GitHub username?",
        max_length=255, blank=True, null=True
        )
    github_url = models.URLField(
        help_text="What is your GitHub URL?",
        max_length=255, blank=True, null=True
        )
    linked_in = models.URLField(
        help_text="What is the URL of your linkedin profile?",
        max_length=255, blank=True, null=True
        )
    portfolio = models.URLField(
        help_text="What is your portfolio URL?",
        max_length=255, blank=True, null=TruePython
        )


class UserProfilePicture(models.Model):
    user = models.ForeignKey(
        User, related_name="profile_pic",
        on_delete=models.CASCADE
        )
    profile_picture = CloudinaryField("profile picture")


class Project(models.Model):
    user = models.ManyToManyField(User)
    # p_language = models.ForeignKey(ProgrammingLanguage)
    title = models.CharField(
        help_text="What is the title for your project?",
        max_length=100
        )
    description = models.TextField(
        help_text="Enter your project description here",
        blank=True, null=True)


class ProgrammingLanguage(models.Model):
    user = models.ManyToManyField(User, blank=True)
    project = models.ManyToManyField(Project, blank=True)
    language = models.CharField(
        help_text="Enter programming language",
        max_length=50
        )

