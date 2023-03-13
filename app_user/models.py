from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from cloudinary import uploader


class User(AbstractUser):
    """Inherits from AbstractUser to gain username, email, first_name,
    last_name and date_joined fields.
    Adds additional specific fields to this model.
    """

    p_language = models.ManyToManyField("ProgramLang")
    location = CountryField(
        help_text="Where do you live?",
        blank_label="Country",
        blank=True,
        null=True,
    )
    github_username = models.CharField(
        help_text="What is your GitHub username?",
        max_length=255,
        blank=True,
        null=True,
    )
    github_url = models.URLField(
        help_text="What is your GitHub URL?",
        max_length=255,
        blank=True,
        null=True,
    )
    linked_in = models.URLField(
        help_text="What is the URL of your linkedin profile?",
        max_length=255,
        blank=True,
        null=True,
    )
    portfolio = models.URLField(
        help_text="What is your portfolio URL?",
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"<user: {self.username}>"

    def to_json(self) -> dict:
        """Function to represent the model as a json object"""
        return {
            "username": self.username,
            "full name": self.get_full_name(),
            "email": self.email,
            "location": self.location.name,
            "github username": self.github_username,
            "github url": self.github_url,
            "linked in url": self.linked_in,
            "portfolio url": self.portfolio,
        }

    def delete(self, *args, **kwargs):
        """
        Additional function to ensure pictures are deleted
        from cloudinary
        """
        # delete associated profile pics
        for pic in self.profile_pic.all():
            pic.delete()
        # then delete itself
        super().delete(*args, **kwargs)


class UserProfilePicture(models.Model):
    user = models.ForeignKey(
        User, related_name="profile_pic", on_delete=models.CASCADE
    )
    profile_picture = CloudinaryField("profile_picture")

    def delete(self, *args, **kwargs):
        """
        Deletes picture from cloudinary as well as just
        the specific db entry
        """
        if self.profile_picture.public_id:
            uploader.destroy(self.profile_picture.public_id)
        super().delete(*args, **kwargs)


class Project(models.Model):
    user = models.ManyToManyField(User, blank=True)
    p_language = models.ManyToManyField("ProgramLang")
    title = models.CharField(
        help_text="What is the title for your project?",
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        help_text="Enter your project description here", blank=True, null=True
    )

    def __str__(self):
        return f"<Project name: {self.title}>"

    def delete(self, *args, **kwargs):
        """
        Additional function to ensure pictures are deleted
        from cloudinary
        """
        # delete associated profile pics
        for pic in self.project_pic.all():
            pic.delete()
        # then delete itself
        super().delete(*args, **kwargs)


class ProjectPicture(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_pic", on_delete=models.CASCADE
    )
    project_picture = CloudinaryField("project_picture")

    def delete(self, *args, **kwargs):
        """
        Deletes picture from cloudinary as well as just
        the specific db entry
        """
        if self.project_picture.public_id:
            uploader.destroy(self.project_picture.public_id)
        super().delete(*args, **kwargs)


class ProgramLang(models.Model):
    language = models.CharField(
        help_text="Enter programming language", max_length=50
    )
    language_icon = CloudinaryField("image", default="p_language_icon")

    def __str__(self):
        return self.language


class Message(models.Model):
    user_sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE
    )
    user_receiver = models.ForeignKey(
        User, related_name="receiver", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True, blank=False)
    edited = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"""<Message from {self.user_sender}
        Subject: {self.title} @{self.sent_date}>"""
