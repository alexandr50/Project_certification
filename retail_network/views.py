from rest_framework import generics

from retail_network.models import RetailNetwork
from retail_network.serializers import RetailNetworkSerializer
from users.permissions import IsUserActive


class RetailNetworksListView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]

class RetailNetworkCreateView(generics.CreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]

class RetailNetworkUpdateView(generics.UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]

class RetailNetworkDeleteView(generics.DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]

class RetailNetworkDetailView(generics.RetrieveAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsUserActive]


