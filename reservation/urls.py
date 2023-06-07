from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
