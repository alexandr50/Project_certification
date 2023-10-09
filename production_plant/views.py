from rest_framework import generics

from production_plant.models import ProductionPlant
from production_plant.serializers import ProductionPlantSerializer
from users.permissions import IsUserActive


class ProductionPlantListView(generics.ListAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
    permission_classes = [IsUserActive]


class ProductionPlantCreateView(generics.CreateAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
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
