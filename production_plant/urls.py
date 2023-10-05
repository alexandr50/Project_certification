from django.urls import path
from .apps import ProductionPlantConfig
from production_plant.views import ProductionPlantCreateView, ProductionPlantUpdateView, ProductionPlantDetailView, \
    ProductionPlantDeleteView, ProductionPlantListView

app_name = ProductionPlantConfig.name

urlpatterns = [
    path('', ProductionPlantListView.as_view(), name='list_productions_plant'),
    path('create/', ProductionPlantCreateView.as_view(), name='create_productions_plant'),
    path('update/<int:pk>/', ProductionPlantUpdateView.as_view(), name='update_productions_plant'),
    path('detail/<int:pk>/', ProductionPlantDetailView.as_view(), name='detail_productions_plant'),
    path('delete/<int:pk>/', ProductionPlantDeleteView.as_view(), name='delete_productions_plant'),
]
