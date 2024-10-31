from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm  # You will create this form next
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# List all stocks with pagination and search
def customer_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the query parameters
    customers = Customer.objects.all()

    # Filter stocks based on the search term
    if search_term:
        customers = customers.filter(name__icontains=search_term)

    paginator = Paginator(customers, 20)  # Show 10 stocks per page
    page_number = request.GET.get('page')

    try:
        customers_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        customers_page = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        customers_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'customer/customer_list.html', {
        'customers': customers_page,
        'search_term': search_term,  # Pass the search term to the template
    })

# View stock detail
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer})

# Create a new stock
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to stock list after creation
    else:
        form = CustomerForm()
    # return render(request, 'stock/stock_create.html', {'form': form})

# Update an existing stock
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    # return render(request, 'customer_list', {'form': form})

# Delete an existing stock
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    # return render(request, 'stock/stock_delete.html', {'stock': stock})
