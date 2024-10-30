from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/new/', views.customer_create, name='customer_create'),
    path('customers/edit/<int:id>/', views.customer_update, name='customer_update'),
     path('customers/delete/<int:id>/', views.customer_delete, name='customer_delete'),  # Delete a supplier
]
