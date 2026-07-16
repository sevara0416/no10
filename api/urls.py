from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()

router.register("posts", PostModelViewSet)

urlpatterns=[
    path("",include(router.urls)),
]


