from django.urls import path
from . import views

urlpatterns = [
    path('trial/', views.index, name= 'index'),
]