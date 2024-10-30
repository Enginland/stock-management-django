from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

# List Suppliers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

# Add or Edit Supplier
def customer_create(request, id=None):
    if id:
        customers = get_object_or_404(Customer, id=id)
    else:
        customers = None

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customers)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customers)
    
    return render(request, 'customer/customer_list.html', {'form': form})


def customer_update(request, id=None):
    if id:
        customers = get_object_or_404(Customer, id=id)  # If ID is provided, update an existing supplier
    else:
        customers = None  # Otherwise, create a new supplier

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customers)
        if form.is_valid():
            form.save()
            if id:
                messages.success(request, 'Customer updated successfully!')
            else:
                messages.success(request, 'Customer added successfully!')
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customers)

    return render(request, 'customer/customer_list.html', {'form': form})

# Delete Supplier (DELETE)
def customer_delete(request, id):
    customers = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customers.delete()
        messages.success(request, 'Customers deleted successfully!')
        return redirect('customer_list')

    return render(request, 'customer/customer_list.html', {'supplier': customers})