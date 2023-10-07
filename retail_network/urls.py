from django.urls import path
from .apps import RetailNetworkConfig
from .views import RetailNetworksListView, RetailNetworkCreateView, RetailNetworkUpdateView, RetailNetworkDetailView, \
    RetailNetworkDeleteView

app_name = RetailNetworkConfig.name

urlpatterns = [
    path('', RetailNetworksListView.as_view(), name='list_productions_plant'),
    path('create/', RetailNetworkCreateView.as_view(), name='create_productions_plant'),
    path('update/<int:pk>/', RetailNetworkUpdateView.as_view(), name='update_productions_plant'),
    path('detail/<int:pk>/', RetailNetworkDetailView.as_view(), name='detail_productions_plant'),
    path('delete/<int:pk>/', RetailNetworkDeleteView.as_view(), name='delete_productions_plant'),
]
