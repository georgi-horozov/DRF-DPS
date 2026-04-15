from django.conf import settings
from django.db import models


class Truck(models.Model):
    plate_number = models.CharField(max_length=20)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="truck",
    )

    def __str__(self):
        return self.plate_number
