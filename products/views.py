from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer, ProductListSerializer


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductsCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer