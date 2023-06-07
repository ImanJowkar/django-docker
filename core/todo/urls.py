from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='my-login'),
    path('profile-management/', views.profile_management, name='profile-management'),
    path('dashboard/', views.dashboard, name='dashboard'),
        
]