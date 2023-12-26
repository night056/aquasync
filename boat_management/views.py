# boat_management/views.py

from rest_framework import generics
from .models import Boat
from .serializers import BoatSerializer

class BoatListCreateView(generics.ListCreateAPIView):
    serializer_class = BoatSerializer

    def get_queryset(self):
        # Filter only available boats for browsing
        return Boat.objects.filter(availability=True, active_status=True)

class BoatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
