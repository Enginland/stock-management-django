from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Supplier
from .forms import SupplierForm  # You will create this form next
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# List all stocks with pagination and search
def supplier_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the query parameters
    suppliers = Supplier.objects.all()

    # Filter stocks based on the search term
    if search_term:
        suppliers = suppliers.filter(name__icontains=search_term)

    paginator = Paginator(suppliers, 20)  # Show 20 stocks per page
    page_number = request.GET.get('page')

    try:
        suppliers_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        suppliers_page = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        suppliers_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'supplier/supplier_list.html', {
        'suppliers': suppliers_page,
        'search_term': search_term,  # Pass the search term to the template
    })

# View stock detail
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'supplier/supplier_detail.html', {'supplier': supplier})

# Create a new stock
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to stock list after creation
    else:
        form = SupplierForm()
    # return render(request, 'stock/stock_create.html', {'form': form})

# Update an existing stock
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    # return render(request, 'customer/customer_detail.html', {'form': form})

# Delete an existing stock
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    # return render(request, 'stock/stock_delete.html', {'stock': stock})
