from django.urls import path     
from . import views

urlpatterns = [
    # This page views the home page.
    path('', views.home, name="homepage"),
    path('register', views.register, name="register"),
    path('success', views.success, name="success"),
    path('error', views.error, name="error"),
    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),    
    
    
    
]
