from django.urls import path
from .apps import ProductsConfig
from .views import ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDetailView, ProductsDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='list_productions_plant'),
    path('create/', ProductsCreateView.as_view(), name='create_productions_plant'),
    path('update/<int:pk>/', ProductsUpdateView.as_view(), name='update_productions_plant'),
    path('detail/<int:pk>/', ProductsDetailView.as_view(), name='detail_productions_plant'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_productions_plant'),
]
