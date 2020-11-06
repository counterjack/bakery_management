from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from bakery.models import Ingredient, Product
from bakery.serializers import (CustomerProductListSerializer,
                                IngredientSerializer, ProductSerializer)
from core.permissions import IsCustomer, IsVendor


class IngredientModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsVendor]
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(bakery=self.request.user.bakery)


class CustomerProductListView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    serializer_class = CustomerProductListSerializer
    queryset = Product.objects.only_active_products()

    def get_queryset(self, *args, **kwargs):
        return Product.objects.only_active_products()

    def get(self, request, *args, **kwargs):
        return Response(CustomerProductListSerializer(self.get_queryset(), many=True).data)


class ProductModelViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, IsVendor]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(CustomerProductListSerializer(self.queryset, many=True))
