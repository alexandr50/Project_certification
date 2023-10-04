from django.urls import path
from .apps import UsersConfig
from users.views import UserCreateView, UserUpdateView, UserDetailView, UserDeleteView, UsersListView

app_name = UsersConfig.name

urlpatterns = [
    path('', UsersListView.as_view(), name='list_users'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail_user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
]
