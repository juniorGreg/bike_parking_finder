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

    def save(self, request):
        data = request.data

        token_data = {
            "secret": settings.GOOGLE_RECAPCHAV3_SECRET,
            "response": data["token"]
        }
        token_verification_request = requests.post("https://www.google.com/recaptcha/api/siteverify", data=token_data)
        if token_verification_request.status_code == 200:
            google_response = token_verification_request.json()
            print(google_response)
            if google_response["success"]:
                del request.data["token"]
                super(CustomRegisterSerializer, self).save(request)
            else:
                raise serializers.ValidationError("token is not valid")
        else:
            print("oki")
            raise serializers.ValidationError("Token validation failed")
