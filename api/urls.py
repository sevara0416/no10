from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter
from .views import PostListView,post_create,PostDetailView, post_update, post_delete

urlpatterns=[
    path("posts/", PostListView),
    path("posts/create/", post_create),
    path("posts/<int:pk>/", PostDetailView),
    path("posts/update/<int:pk>/", post_update),
    path("posts/delete/<int:pk>/", post_delete),
]


