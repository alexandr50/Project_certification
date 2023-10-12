from rest_framework import generics

from production_plant.models import ProductionPlant
from production_plant.pagination import BaseNetworkPagination
from production_plant.serializers import ProductionPlantSerializer, ProductionPlantCreateSerializer
from users.permissions import IsUserActive


class ProductionPlantListView(generics.ListAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantCreateSerializer
    permission_classes = [IsUserActive]
    filterset_fields = ['contact__city', ]
    pagination_class = BaseNetworkPagination


class ProductionPlantCreateView(generics.CreateAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantCreateSerializer
    permission_classes = [IsUserActive]


class ProductionPlantUpdateView(generics.UpdateAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
    permission_classes = [IsUserActive]


class ProductionPlantDetailView(generics.RetrieveAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
    permission_classes = [IsUserActive]


class ProductionPlantDeleteView(generics.DestroyAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
    permission_classes = [IsUserActive]
