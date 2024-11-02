from django.contrib import admin

# Register your models here.
from .models import Stock, StockTransaction
# apps/inventory/admin.py
from django.contrib import admin
from .models import Stock, StockTransaction  # Replace 'Item' with 'Stock'

# Register your models with the Django admin site
admin.site.register(Stock)
admin.site.register(StockTransaction)

# @admin.register(Stock)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'quantity_in_stock', 'updated_at')
#     search_fields = ('name',)

# @admin.register(StockTransaction)
# class StockTransactionAdmin(admin.ModelAdmin):
#     list_display = ('item', 'transaction_type', 'quantity', 'timestamp')
#     list_filter = ('transaction_type', 'timestamp')
