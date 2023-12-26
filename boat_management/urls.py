# boat_management/urls.py

from django.urls import path
from .views import BoatListCreateView, BoatDetailView

urlpatterns = [
    path('boats/', BoatListCreateView.as_view(), name='boat-list-create'),
    path('boats/<str:pk>/', BoatDetailView.as_view(), name='boat-detail'),
]
