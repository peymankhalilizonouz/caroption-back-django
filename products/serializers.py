from rest_framework.serializers import ModelSerializer, StringRelatedField

from products.models import Product


class ProductSerializer(ModelSerializer):
    brand = StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
