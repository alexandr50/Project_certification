from rest_framework import generics

from production_plant.models import ProductionPlant
from production_plant.serializers import ProductionPlantSerializer



class ProductionPlantListView(generics.ListAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer


class ProductionPlantCreateView(generics.CreateAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer


class ProductionPlantUpdateView(generics.UpdateAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer


class ProductionPlantDetailView(generics.RetrieveAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer


class ProductionPlantDeleteView(generics.DestroyAPIView):
    queryset = ProductionPlant.objects.all()
    serializer_class = ProductionPlantSerializer
