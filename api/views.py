from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializers

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializers

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class= PostSerializers