from rest_framework import serializers

from production_plant.models import ProductionPlant
from products.models import Product
from retail_network.models import RetailNetwork
from solo_trader.models import SoleTrader


class ProductListSerializer(serializers.ModelSerializer):
    production_plant_prod = serializers.SerializerMethodField()
    retail_network_prod = serializers.SerializerMethodField()
    solo_trader_prod = serializers.SerializerMethodField()

    def get_production_plant_prod(self, obj):
        return [ob.title for ob in ProductionPlant.objects.filter(id=obj.id)]

    def get_retail_network_prod(self, obj):
        return [ob.title for ob in RetailNetwork.objects.filter(id=obj.id)]

    def get_solo_trader_prod(self, obj):
        return [ob.title for ob in SoleTrader.objects.filter(id=obj.id)]





    class Meta:
        model = Product
        fields = ('title', 'model', 'release', 'production_plant_prod', 'retail_network_prod', 'solo_trader_prod')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release')
