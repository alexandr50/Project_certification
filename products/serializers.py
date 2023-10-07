from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    production_plant = serializers.SerializerMethodField()

    def get_production_plant(self, obj):
        return obj.production_plant.title

    class Meta:
        model = Product
        fields = ('title', 'model', 'release', 'production_plant')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release', 'production_plant')
