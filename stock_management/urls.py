"""
URL configuration for stock_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # For built-in authentication views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URLs
    path('home', include('main.urls')),  # Main app URLs at root path
    path('stock/', include('apps.stock.urls')),  # Stock app URLs
    path('inventory/', include('apps.inventory.urls')),  # Inventory app URLs
    path('customer/', include('apps.customer.urls')),  # Customer app URLs
    path('supplier/', include('apps.supplier.urls')),  # Supplier app URLs
    
    # User authentication paths (login, logout, password reset, etc.)
    path('', include('apps.users.urls')),  # Include accounts app URLs for login, register, profile
]

