from django.contrib import admin
from django.urls import path, include

from Comment_blog.views import ArticleEditView, IndexView, ArtticleDetailView,CommentsEditView

app_name = "Comment_blog"

urlpatterns = [
    path(r"",IndexView.as_view(),name="index"),
    path(r"articleDetail/<int:pk>/<str:title>/",ArtticleDetailView.as_view(),name="articleDetail"),
    path(r"drawArticle/",ArticleEditView.as_view(),name="articleEdit"),
    path(r"comentEdit",CommentsEditView.as_view(),name="commentEdit"),
    path(r"articleEdit/",ArticleEditView.as_view(),name="articleEdit")
]