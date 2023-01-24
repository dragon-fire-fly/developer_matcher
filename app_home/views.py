from django.shortcuts import render
from django.views.generic import TemplateView
from app_user.models import User

# Create your views here.


class HomeView(TemplateView):
    model = User
    template_name = "app_home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
