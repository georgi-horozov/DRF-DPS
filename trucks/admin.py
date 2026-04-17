from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Truck

# admin.site.register(Truck)

UserModel = get_user_model()

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('id', 'plate_number', 'owner')
    ordering = ('id',)
