from django.contrib import admin
from django.urls import path, include
from .import views
app_name = 'lang'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    
]