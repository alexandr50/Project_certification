from django.urls import path
from .apps import SoloTraderConfig
from .views import SoleTradersListView, SoleTraderCreateView, SoleTraderUpdateView, SoleTraderDetailView, \
    SoleTraderDeleteView

app_name = SoloTraderConfig.name

urlpatterns = [
    path('', SoleTradersListView.as_view(), name='list_productions_plant'),
    path('create/', SoleTraderCreateView.as_view(), name='create_productions_plant'),
    path('update/<int:pk>/', SoleTraderUpdateView.as_view(), name='update_productions_plant'),
    path('detail/<int:pk>/', SoleTraderDetailView.as_view(), name='detail_productions_plant'),
    path('delete/<int:pk>/', SoleTraderDeleteView.as_view(), name='delete_productions_plant'),
]
