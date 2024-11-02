from django.urls import path
from .views import inventory_list, item_detail, update_stock

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', item_detail, name='item_detail'),
    path('update/<int:stock_id>/', update_stock, name='update_stock'),
]
