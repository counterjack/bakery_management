from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from core.permissions import IsCustomer, IsVendor
from bakery.models import Product
from rest_framework.response import Response
from bakery.serializers import CustomerProductListSerializer, ProductSerializer
# Create your views here.


class CustomerProductListView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    serializer_class = [CustomerProductListSerializer]
    queryset = Product.objects.only_active_products()

    def get(self, request, *args, **kwargs):
        return Response(CustomerProductListSerializer(self.queryset, many=True))


class ProductModelViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, IsVendor]
    serializer_class = [ProductSerializer]
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(CustomerProductListSerializer(self.queryset, many=True))

