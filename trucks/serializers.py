from rest_framework import serializers

from locations.serializers import LocationSerializer

from .models import Truck


class TruckSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    class Meta:
        model = Truck
        fields = ["id", "plate_number", "locations"]