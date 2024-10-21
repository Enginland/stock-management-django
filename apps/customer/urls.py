from django.urls import path
from .views import customer_list, customer_detail, customer_create, customer_update, customer_delete

urlpatterns = [
    path('', customer_list, name='customer_list'),  # List all customers
    path('<int:customer_id>/', customer_detail, name='customer_detail'),  # View customer details
    path('create/', customer_create, name='customer_create'),  # Create new customer
    path('update/<int:customer_id>/', customer_update, name='customer_update'),  # Update customer
    path('customer/<int:customer_id>/delete/', customer_delete, name='customer_delete'),
]