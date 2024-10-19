from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Stock
from .forms import StockForm  # You will create this form next
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# List all stocks with pagination and search
def stock_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the query parameters
    stocks = Stock.objects.all()

    # Filter stocks based on the search term
    if search_term:
        stocks = stocks.filter(name__icontains=search_term)

    paginator = Paginator(stocks, 10)  # Show 10 stocks per page
    page_number = request.GET.get('page')

    try:
        stocks_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        stocks_page = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        stocks_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'stock/stock_list.html', {
        'stocks': stocks_page,
        'search_term': search_term,  # Pass the search term to the template
    })

# View stock detail
def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock/stock_detail.html', {'stock': stock})

# Create a new stock
def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')  # Redirect to stock list after creation
    else:
        form = StockForm()
    return render(request, 'stock/stock_create.html', {'form': form})

# Update an existing stock
def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock/stock_update.html', {'form': form})

# Delete an existing stock
def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'stock/stock_delete.html', {'stock': stock})
