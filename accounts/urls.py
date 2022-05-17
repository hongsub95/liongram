from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [path("signup/", views.SignupView, name="signup"),
               path("login/", views.LoginView.as_view(), name="login"),
               path("logout/", views.log_out, name="logout")]