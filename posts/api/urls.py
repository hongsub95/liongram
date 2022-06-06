from django.urls import path,include
from rest_framework import routers
from .views import QnAViewset

app_name = "api_posts"


router = routers.DefaultRouter()
router.register("",QnAViewset)

urlpatterns = [
    path('',include(router.urls))
]

"""
urlpatterns = [
    path("posts/",QnAListView.as_view(),name ="posts_list"),
    path("posts/<int:pk>/",QnARetrieveView.as_view(),name="posts_retrieve"),
    path("comment/",CommentListView.as_view())
]
"""