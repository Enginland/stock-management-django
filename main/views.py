from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')  # This renders base.html

# def open(request):
#     return render(request, 'open.html')  # Ensure you have a open.html template