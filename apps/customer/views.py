from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# List Customers
def customer_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the query parameters
    customer = Customer.objects.all()

    # Filter stocks based on the search term
    if search_term:
        customer = customer.filter(name__icontains=search_term)

    paginator = Paginator(customer, 20)  # Show 10 stocks per page
    page_number = request.GET.get('page')

    try:
        customer_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        customer_page = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        customer_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'customer/customer_list.html', {
        'customer': customer_page,
        'search_term': search_term,  # Pass the search term to the template
    })
# Add or Edit Customer
def customer_create(request, id=None):
    if id:
        customer = get_object_or_404(Customer, id=id)
    else:
        customer = None

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            if id:
                messages.success(request, 'Customer updated successfully!')
            else:
                messages.success(request, 'Customer added successfully!')
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customer/customer_list.html', {'form': form})

# Update Customer
def customer_update(request, id=None):
    if id:
        customer = get_object_or_404(Customer, id=id)
    else:
        customer = None

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully!' if id else 'Customer added successfully!')
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer/customer_list.html', {'form': form})

# Delete Customer
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('customer_list')

    return render(request, 'customer/customer_list.html', {'customer': customer})
