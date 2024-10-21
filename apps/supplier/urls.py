from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/new/', views.supplier_create, name='supplier_create'),
    path('suppliers/edit/<int:id>/', views.supplier_update, name='supplier_update'),
     path('suppliers/delete/<int:id>/', views.supplier_delete, name='supplier_delete'),  # Delete a supplier
]
