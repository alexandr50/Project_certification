from rest_framework import generics

from production_plant.pagination import BaseNetworkPagination
from solo_trader.models import SoleTrader
from solo_trader.serializers import SoleTraderCreateSerializer, SoloTraderSerializer, SoloTraderUpdateSerializer
from users.permissions import IsUserActive


class SoleTradersListView(generics.ListAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoloTraderSerializer
    permission_classes = [IsUserActive]
    filterset_fields = ['contact__city', ]
    pagination_class = BaseNetworkPagination

class SoleTraderCreateView(generics.CreateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]

class SoleTraderUpdateView(generics.UpdateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoloTraderUpdateSerializer
    permission_classes = [IsUserActive]

class SoleTraderDeleteView(generics.DestroyAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]

class SoleTraderDetailView(generics.RetrieveAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]


