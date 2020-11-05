from rest_framework import serializers
from bakery.models import Bakery, ProductIngredient, Product


class BakerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bakery


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
