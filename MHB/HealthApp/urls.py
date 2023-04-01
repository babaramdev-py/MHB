from django.urls import path
from . import views

urlpatterns = [
    path('ai/',views.AIView,name="AI page"),
    path('therapist/',views.TherapistListView.as_view(),name="therapist")
]