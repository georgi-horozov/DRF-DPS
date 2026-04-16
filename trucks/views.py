from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from trucks.serializers import TruckSerializer

from .models import Truck


class TruckViewset(viewsets.ModelViewSet):
    # queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Truck.objects.filter(owner=self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

