from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


class ProgrammingLanguage(models.Model):
    language = models.CharField(help_text="Enter programming language", max_length=50)

    def __str__(self):
        return self.language


class User(AbstractUser):
    """Inherits from AbstractUser to gain username, email, first_name,
    last_name and date_joined fields.
    Adds additional specific fields to this model.
    """

    p_language = models.ManyToManyField(ProgrammingLanguage)
    location = CountryField(
        help_text="Where do you live?", blank_label="Country", blank=True, null=True
    )
    github_username = models.CharField(
        help_text="What is your GitHub username?", max_length=255, blank=True, null=True
    )
    github_url = models.URLField(
        help_text="What is your GitHub URL?", max_length=255, blank=True, null=True
    )
    linked_in = models.URLField(
        help_text="What is the URL of your linkedin profile?",
        max_length=255,
        blank=True,
        null=True,
    )
    portfolio = models.URLField(
        help_text="What is your portfolio URL?", max_length=255, blank=True, null=True
    )
    # Users that a user follows. Don't have to follow anyone and don't need to 
    # be followed back by the same user.
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
        )

    def __str__(self):
        return f"<user: {self.username}>"


class UserProfilePicture(models.Model):
    user = models.ForeignKey(User, related_name="profile_pic", on_delete=models.CASCADE)
    profile_picture = CloudinaryField("profile picture")


class Project(models.Model):
    user = models.ManyToManyField(User)
    p_language = models.ManyToManyField(ProgrammingLanguage)
    title = models.CharField(
        help_text="What is the title for your project?", max_length=100
    )
    description = models.TextField(
        help_text="Enter your project description here", blank=True, null=True
    )

    def __str__(self):
        return f"<Project name: {self.title}>"
