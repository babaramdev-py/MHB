from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="AI page")
]