from django.db import models

from trucks.models import Truck


class Location(models.Model):
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='locations')
