from django.shortcuts import render
from .models import BikeParking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BikeParkingSerializer
from django.contrib.gis.measure import Distance, D
from django.contrib.gis.geos import Point
from django.conf import settings

# Create your views here.
def index(request):
    context = {"static_url": settings.STATIC_URL, "google_recaptcha_site": settings.GOOGLE_RECAPCHAV3_SITE}
    print(context)
    return render(request, "api/index.html", context)


@api_view(['GET'])
def bike_parkings(request):
    distance = float(request.GET.get("radius", "5000"))
    lat = float(request.GET.get("lng", '45.5016889'))
    lng = float(request.GET.get("lat", "-73.567256"))
    point = Point(lat, lng)
    bike_parkings = BikeParking.objects.filter(position__distance_lte=(point, D(m=distance)))
    serializer = BikeParkingSerializer(bike_parkings, many=True)
    return Response(serializer.data)
