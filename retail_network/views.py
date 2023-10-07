from rest_framework import generics

from retail_network.models import RetailNetwork
from retail_network.serializers import RetailNetworkSerializer


class RetailNetworksListView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer

class RetailNetworkCreateView(generics.CreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer

class RetailNetworkUpdateView(generics.UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer

class RetailNetworkDeleteView(generics.DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer

class RetailNetworkDetailView(generics.RetrieveAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


