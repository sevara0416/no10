from django.shortcuts import render
from .models import Post
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializers
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def PostListView(request):
    posts=Post.objects.all()
    serializer=PostSerializers(posts, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def post_create(request):
    if request.method == "GET":
        return Response({"message": "POST request yuborn"})
    serializer = PostSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def PostDetailView(request, pk):
    post=Post.objects.get(pk=pk)
    serializer=PostSerializers(post)
    return Response(serializer.data)


@api_view(["PATCH","PUT"])
def post_update(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == "PUT":
        serializer= PostSerializers(post, data=request.data)
    else:
        serializer = PostSerializers(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return Response({"message":"post ochirld"}, status=status.HTTP_204_NO_CONTENT)






# @api_view(["POST"])
# def PostCreateView(request):
#     serializer=PostSerializers(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response({"yaratishda muammo":"malumot xato kiritildi yoki umuman krtlmadi"})




# class PostModelViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class= PostSerializers