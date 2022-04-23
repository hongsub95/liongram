from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("QnA/", views.QnA, name="QnA"),
    path("int:<pk>/", views.QnA_detail.as_view(), name="QnA_detail"),
    path("int:<qna_pk>/comment/", views.Comment, name="comment"),
]
