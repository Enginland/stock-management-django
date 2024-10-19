from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm  # Your custom form
from django.contrib.auth.decorators import login_required
from django.urls import reverse  # To use the URL name for redirecting

def open(request):
    return render(request, 'open.html')  # Ensure you have a open.html template
# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main:index'))  # Redirect to the main page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Login view (you can adjust it or use Django's built-in login view)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:index'))  # Redirect to the main page after login
    return render(request, 'users/login.html')
