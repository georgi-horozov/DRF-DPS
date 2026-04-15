from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from trucks.views import TruckViewset

router = DefaultRouter()
router.register("", TruckViewset, basename="trucks")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("trucks/", include(router.urls))
]
