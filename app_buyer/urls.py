from django.urls import path
from app_buyer import views
urlpatterns = [
  
path('', views.index, name='index'),
path('login/', views.login, name='login'),
path('register/', views.register, name='register'),
path('contact/', views.contact, name='contact'),


]