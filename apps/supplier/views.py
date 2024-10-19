from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'supplier/list.html')  # Ensure the template exists
