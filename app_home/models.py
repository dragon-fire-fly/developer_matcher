from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Inherits from AbstractUser to gain username, email, first_name,
    last_name and date_joined fields.
    Adds additional specific fields to this model.
    '''
    location = models.CharField(
        help_text="Where do you live?",
        max_length=255
        )
    github_user = models.CharField(
        help_text="What is your GitHub username?",
        max_length=255
        )
    github_url = models.CharField(
        help_text="What is your GitHub URL?",
        max_length=255
        )
    linked_in = models.CharField(
        help_text="What is the URL of your linkedin profile?",
        max_length=255
        )
    portfolio = models.CharField(
        help_text="What is your portfolio URL?",
        max_length=255
        )