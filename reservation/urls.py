from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='menu_detail'),
]
