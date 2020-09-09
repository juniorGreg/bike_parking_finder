from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import BikeParking

# Register your models here.
@admin.register(BikeParking)
class BikeParkingAdmin(OSMGeoAdmin):
    default_lon =  -73590854
    default_lat =  45501372
    default_zoom = 12
