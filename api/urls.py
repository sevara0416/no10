from django.urls import path
from .views import PostListView,post_create,PostDetailView, post_update, post_delete,RegisterAPIView,ProfileAPIView,LogoutAPIView
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)


urlpatterns=[
    path("posts/", PostListView),
    path("posts/create/", post_create),
    path("posts/<int:pk>/", PostDetailView),
    path("posts/update/<int:pk>/", post_update),
    path("posts/delete/<int:pk>/", post_delete),
    path("register/", RegisterAPIView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
]
