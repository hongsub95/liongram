from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("QnA/", views.QnA, name="QnA"),
    path("<int:pk>/", views.QnA_detail.as_view(), name="QnA_detail"),
    path("<int:qna_pk>/comment/", views.Comment, name="comment"),
    path("<int:qna_pk>/edit/", views.QnAUpdateView.as_view(), name="QnA_edit"),
    path("<int:qna_pk>/delete/", views.QnA_delete, name="QnA_delete"),
    path(
        "<int:qna_pk>/comment/<int:comment_pk>/delete/",
        views.Comment_Delete.as_view(),
        name="comment_delete",
    ),
    path(
        "<int:qna_pk>/comment/<int:comment_pk>/edit/",
        views.Comment_edit,
        name="comment_edit",
    ),
    path(
        "<int:qna_pk>/comment/<int:comment_pk>/update/",
        views.Comment_update,
        name="comment_update",
    ),
]
