from rest_framework.serializers import ModelSerializer

from .models import Post

class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "comment", "likes","author", "created_at",]
        read_only_fields=["id", "created_at"]

