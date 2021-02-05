from .models import BikeParking
from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer
import requests

from django.conf import settings

class BikeParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeParking
        fields = "__all__"

class CustomRegisterSerializer(RegisterSerializer):

    token = serializers.CharField()

    def validate_token(self, token):
        token_data = {
            "secret": settings.GOOGLE_RECAPCHAV3_SECRET,
            "response": token
        }

        token_verification_request = requests.post("https://www.google.com/recaptcha/api/siteverify", data=token_data)
        if token_verification_request.status_code == 200:
            google_response = token_verification_request.json()
            print(google_response)
            if google_response["success"]:
                return token

        raise serializers.ValidationError("You are a robot.")
