from rest_framework import serializers

from solo_trader.models import SoleTrader


class SoleTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoleTrader
        fields = ('title',)
