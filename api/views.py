from django.shortcuts import render
from .models import BikeParking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BikeParkingSerializer
from django.contrib.gis.measure import Distance, D
from django.contrib.gis.geos import Point
from django.conf import settings
from django.shortcuts import redirect

from allauth.socialaccount.models import SocialLogin


# Create your views here.
def index(request):
    context = {}

    if "google_code" in request.session:
        context["google_code"] = request.session["google_code"]

    if "facebook_code" in request.session:
        context["facebook_code"] = request.session["facebook_code"]


    context["static_url"] = settings.STATIC_URL
    context["google_recaptcha_site"] = settings.GOOGLE_RECAPCHAV3_SITE
    #print(context)
    return render(request, "api/index.html", context)

def google_callback(request):
    code = request.GET.get("code")

    request.session["google_code"] = code
    #print(context)
    return redirect("index")

def facebook_callback(request):
    code = request.GET.get("code")

    request.session["facebook_code"] = code
    #print(context)
    return redirect("index")


def social_signup(request):
    user = SocialLogin.deserialize(request.session["socialaccount_sociallogin"])

    return render(request, 'api/socialaccount_signup.html')


@api_view(['GET'])
def bike_parkings(request):
    distance = float(request.GET.get("radius", "5000"))
    lat = float(request.GET.get("lng", '45.5016889'))
    lng = float(request.GET.get("lat", "-73.567256"))
    point = Point(lat, lng)
    bike_parkings = BikeParking.objects.filter(position__distance_lte=(point, D(m=distance)))
    serializer = BikeParkingSerializer(bike_parkings, many=True)
    return Response(serializer.data)

def confirm_email(request, key):
    context = {
        "key": key
    }
    return render(request, "api/email_confirmation.html", context)
