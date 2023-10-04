from rest_framework import serializers

from production_plant.models import ProductionPlant


class ProductionPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlant
        fields = ('title',)