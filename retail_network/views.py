from rest_framework import generics

from production_plant.pagination import BaseNetworkPagination
from retail_network.models import RetailNetwork
from retail_network.serializers import RetailNetworkCreateSerializer, RetailNetworkSerializer, \
    RetailNetworkUpdateSerializer
from users.permissions import IsUserActive


class RetailNetworksListView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]
    filterset_fields = ['contact__city', ]
    pagination_class = BaseNetworkPagination

class RetailNetworkCreateView(generics.CreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkCreateSerializer
    permission_classes = [IsUserActive]

class RetailNetworkUpdateView(generics.UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkUpdateSerializer
    permission_classes = [IsUserActive]

class RetailNetworkDeleteView(generics.DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkCreateSerializer
    permission_classes = [IsUserActive]

class RetailNetworkDetailView(generics.RetrieveAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkCreateSerializer
    permission_classes = [IsUserActive]


