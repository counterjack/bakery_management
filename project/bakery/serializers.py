from rest_framework import serializers
from bakery.models import Bakery, ProductIngredient, Product, Ingredient
from rest_framework.exceptions import ValidationError

class BakerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bakery
        fields = ("name", "address")

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = "__all__"

class ProductIngredientDetailSerializer(serializers.Serializer):
    ingredient_name = serializers.CharField(source="ingredient__name", read_only=True)
    ingredient_description = serializers.CharField(source="ingredient__description", read_only=True)
    percentage = serializers.CharField()
    quantity = serializers.CharField()
    id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ("ingredient_name", "ingredient_description", "percentage", "quantity", "id")


class ProductIngredientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductIngredient
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    ingredients = ProductIngredientDetailSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):

        ingredients = validated_data.pop("ingredients")
        bakery = validated_data["bakery"]
        bakery = Bakery.objects.get(id=bakery.id)
        # Check if the ingredients are from the current bakery list or not
        available_ingredients_ids = bakery.ingredients.values_list("id", flat=True)

        for item in ingredients:
            if item["id"] not in available_ingredients_ids:
                raise ValidationError("Invalid ingredient for bakery.")
        # create product first
        new_product = Product.objects.create(**validated_data)
        # now, insert the date to ProductIngredient relation model
        #TODO: Use model serializer here instead of below
        for item in ingredients:
            ingredient_id = item.pop("id")
            ProductIngredient.objects.create(
                product=new_product, ingredient_id=ingredient_id, **item
            )

        return new_product

class CustomerProductListSerializer(serializers.ModelSerializer):
    bakery = BakerySerializer()
    class Meta:
        model = Product
        exclude = ("cost", "is_active")


class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(source="ingredient")
    class Meta:
        model = ProductIngredient