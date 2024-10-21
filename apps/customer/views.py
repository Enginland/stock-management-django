from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps import customer
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Value
from django.db.models.functions import Concat

# List all customers
def customer_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the query parameters
    customers = Customer.objects.all()

    # Filter stocks based on the search term
    if search_term:
        # Combine first_name and last_name and then filter using the search term
        customers = customers.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).filter(full_name__icontains=search_term)

    paginator = Paginator(customers, 20)  # Show 10 stocks per page
    page_number = request.GET.get('page')

    try:
        customers_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        customers_page = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        customers_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'customer/customer_list.html', {
        'stocks': customers_page,
        'search_term': search_term,  # Pass the search term to the template
        
    })
# Customer details view
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    # return render(request, 'customer/customer_detail.html', {'customer': customer})

# Create a new customer
def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    # return render(request, 'customer/customer_form.html', {'form': form})

# Update an existing customer
def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    # return render(request, 'customer/customer_form.html', {'form': form})

# Delete an existing Customer
def customer_delete(request, customer_id):
    Customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        Customer.delete()
        return redirect('customer_list')
    # return render(request, 'stock/stock_delete.html', {'stock': stock})