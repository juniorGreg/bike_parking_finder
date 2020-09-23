from .models import BikeParking
from rest_framework import serializers


class BikeParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeParking
        fields = "__all__"
