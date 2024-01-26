from django.urls import path
from . import views

# list save path

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact')
]