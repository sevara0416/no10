from rest_framework.serializers import ModelSerializer

from .models import Product

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "descriptions", "created_at",]
        read_only_fields=["id", "created_at"]

