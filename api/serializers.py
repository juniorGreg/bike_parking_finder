from .models import BikeParking
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
import requests

class BikeParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeParking
        fields = "__all__"

class CustomRegisterSerializer(RegisterSerializer):
    token = serializers.CharField()

    def validate_token(self, token):
        pass
