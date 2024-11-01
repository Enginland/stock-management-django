
from django.urls import path
from .views import supplier_list, supplier_detail, supplier_create, supplier_update, supplier_delete

urlpatterns = [
    path('', supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/', supplier_detail, name='supplier_detail'),
    path('supplier/create/', supplier_create, name='supplier_create'),
    path('supplier/<int:pk>/update/', supplier_update, name='supplier_update'),
    path('supplier/<int:pk>/delete/', supplier_delete, name='supplier_delete'),
]
