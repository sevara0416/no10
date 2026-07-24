from django.shortcuts import render
from .models import Post, CustomUser
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer,RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"username": request.user.username, "email":request.user.email,})

class LogoutAPIView(APIView):
    permission_classes= [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token=request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message":"Logout seccessfil"}, status=status.HTTP_205_RESET_CONTENT)

        except Exception:
            return Response({"error":"Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def PostListView(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def post_create(request):
    if request.method == "GET":
        return Response({"message": "POST request yuborn"})
    serializer = PostSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def PostDetailView(request, pk):
    post=Post.objects.get(pk=pk)
    serializer=PostSerializer(post)
    return Response(serializer.data)


@api_view(["PATCH","PUT"])
def post_update(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == "PUT":
        serializer= PostSerializer(post, data=request.data)
    else:
        serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return Response({"message":"post ochirld"}, status=status.HTTP_204_NO_CONTENT)

