from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from locations.serializers import LocationSerializer

from .models import Location


class LocationViewset(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    # queryset = Location.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Location.objects.filter(truck__owner=self.request.user)


