from django import forms
from django.forms import ModelForm, ValidationError
from app_user.models import Project, ProjectPicture, ProgrammingLanguage





class ProjectCreationForm(forms.ModelForm):
    p_language_objects = ProgrammingLanguage.objects.all()
    lang_choices = []
    n = 0
    for lang in p_language_objects:
        n += 1
        lang_choices.append((n, lang.language))

    p_language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=lang_choices)
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
