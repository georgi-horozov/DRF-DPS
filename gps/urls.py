from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from locations.views import LocationViewset
from trucks.views import TruckViewset

router = DefaultRouter()
router.register("trucks", TruckViewset, basename="trucks")
router.register("locations", LocationViewset, basename="locations")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("", include(router.urls))
]
