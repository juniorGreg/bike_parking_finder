from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import BikeParking

# Register your models here.
@admin.register(BikeParking)
class BikeParkingAdmin(OSMGeoAdmin):
    default_lon = -82090854
    default_lat = 57001372
    default_zoom = 12
