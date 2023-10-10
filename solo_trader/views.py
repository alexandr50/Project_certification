from rest_framework import generics

from solo_trader.models import SoleTrader
from solo_trader.serializers import SoleTraderCreateSerializer, SoloTraderSerializer
from users.permissions import IsUserActive


class SoleTradersListView(generics.ListAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoloTraderSerializer
    permission_classes = [IsUserActive]

class SoleTraderCreateView(generics.CreateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]

class SoleTraderUpdateView(generics.UpdateAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]

class SoleTraderDeleteView(generics.DestroyAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]

class SoleTraderDetailView(generics.RetrieveAPIView):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderCreateSerializer
    permission_classes = [IsUserActive]


