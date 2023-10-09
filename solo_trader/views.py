from rest_framework import generics

from solo_trader.models import SoleTrader
from solo_trader.serializers import SoleTraderSerializer


class SoleTradersListView(generics.ListAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer

class SoleTraderCreateView(generics.CreateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer

class SoleTraderUpdateView(generics.UpdateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer

class SoleTraderDeleteView(generics.DestroyAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer

class SoleTraderDetailView(generics.RetrieveAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer


