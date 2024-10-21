from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier
from .forms import SupplierForm

# List Suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})

# Add or Edit Supplier
def supplier_create(request, id=None):
    if id:
        supplier = get_object_or_404(Supplier, id=id)
    else:
        supplier = None

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    
    return render(request, 'supplier/supplier_list.html', {'form': form})

# Add or Edit Supplier (CREATE / UPDATE)
def supplier_update(request, id=None):
    if id:
        supplier = get_object_or_404(Supplier, id=id)  # If ID is provided, update an existing supplier
    else:
        supplier = None  # Otherwise, create a new supplier

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            if id:
                messages.success(request, 'Supplier updated successfully!')
            else:
                messages.success(request, 'Supplier added successfully!')
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'supplier/supplier_list.html', {'form': form})

# Delete Supplier (DELETE)
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)

    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Supplier deleted successfully!')
        return redirect('supplier_list')

    return render(request, 'supplier/supplier_list.html', {'supplier': supplier})