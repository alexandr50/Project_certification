from rest_framework import serializers

from retail_network.models import RetailNetwork


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = ('title',  'email', 'country', 'city', 'street', 'number_home', 'supplier', 'debt')
