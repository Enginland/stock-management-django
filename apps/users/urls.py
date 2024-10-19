from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.open, name='open'),  # Replace with your actual view
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Login
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # Logout
     path('logout/', auth_views.LogoutView.as_view(next_page='open'), name='logout'),  # Logout
    path('register/', views.register, name='register'),  # User registration
    path('register/', views.register, name='register'),  # User registration
    path('profile/', views.profile, name='profile'),  # User profile view
    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
