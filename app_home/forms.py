from django import forms
from django.forms import ModelForm, ValidationError
from app_user.models import Project, ProjectPicture, ProgramLang
from django.contrib import messages
from better_profanity import profanity


def validate_project_name(data):
    """Checks that a project name is not already taken and does not
    contain profanities"""

    if isinstance(data, str):
        project_name = data
    else:
        project_name = data.cleaned_data.get("title", None)
        if not project_name:
            raise ValidationError("No title given")
        else:
            if data.instance:
                if data.instance.title == project_name:
                    return

    # Check project name for profanity and do not allow if present
    if profanity.contains_profanity(project_name):
        raise ValidationError("profanity")
    else:
        # Check if project name already taken and return error if so
        try:
            taken_project_name = Project.objects.get(title=project_name)
            raise ValidationError("duplicate_name")
        except Project.DoesNotExist:
            return


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["p_language", "title", "description"]

    def save(self, commit=True):
        project = super(ProjectCreationForm, self).save(commit=False)
        if commit:
            project.save()
        return project

    def clean(self):
        validate_project_name(self)


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["p_language", "title", "description"]

    def save(self, commit=True):
        project = super(ProjectEditForm, self).save(commit=False)
        if commit:
            project.save()
        return project

    def clean(self):
        validate_project_name(self)


class AddProjectPictureForm(forms.ModelForm):
    class Meta:
        model = ProjectPicture
        fields = "__all__"
        exclude = ["project"]
