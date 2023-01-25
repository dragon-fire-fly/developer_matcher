from django.urls import path
from django.views.generic import TemplateView
from .views import SignupView

app_name = "app_user"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("success/", TemplateView.as_view(template_name="app_user/success.html"), name="success"),
]
