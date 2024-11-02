from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock, StockTransaction
from django.utils import timezone

# View all items
def inventory_list(request):
    items = Stock.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

# View item details
def item_detail(request, pk):
    item = get_object_or_404(Stock, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': item})

# Update stock for an item
def update_stock(request, pk):
    item = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        quantity = int(request.POST.get('quantity'))
        
        # Update quantity in stock
        if transaction_type == 'IN':
            item.quantity_in_stock += quantity
        elif transaction_type == 'OUT':
            item.quantity_in_stock -= quantity

        # Create stock transaction record
        StockTransaction.objects.create(
            item=item,
            transaction_type=transaction_type,
            quantity=quantity,
            timestamp=timezone.now()
        )
        item.save()
        return redirect('inventory_list')
    
    return render(request, 'inventory/update_stock.html', {'item': item})
