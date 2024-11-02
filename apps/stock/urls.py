# apps/stock/urls.py

from django.urls import path
from main import views  # Make sure you have the correct views imported

from django.urls import path
from .views import generate_pdf_report, stock_list, stock_detail, stock_create, stock_update, stock_delete

urlpatterns = [
    path('', stock_list, name='stock_list'),
    path('stock/<int:pk>/', stock_detail, name='stock_detail'),
    path('stock/create/', stock_create, name='stock_create'),
    path('stock/<int:pk>/update/', stock_update, name='stock_update'),
    path('stock/<int:pk>/delete/', stock_delete, name='stock_delete'),
    path('reports/stock/pdf/', generate_pdf_report, name='generate_pdf_report'),

]
