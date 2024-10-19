# apps/stock/urls.py

from django.urls import path
from main import views  # Make sure you have the correct views imported

urlpatterns = [
    path('', views.home, name='home'),  # Replace with your actual view
    # Add more paths as needed
]
