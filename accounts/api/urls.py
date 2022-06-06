from django.urls import path,include
from rest_framework import routers
from . import views

app_name = "api_accounts"

"""
router = routers.DefaultRouter()
router.register("",views.login_view)
"""
urlpatterns = [path('',views.LoginView.as_view()),]