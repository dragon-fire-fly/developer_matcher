from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView

app_name = "app_user"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("success/", TemplateView.as_view(template_name="app_user/success.html"), name="success"),
]
