from django.urls import path
from . import views

urlpatterns = [
    path('ai/',views.AIView,name="AI page")
]