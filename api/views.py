from django.shortcuts import render
from .models import BikeParking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BikeParkingSerializer
from django.contrib.gis.measure import Distance, D
from django.contrib.gis.geos import Point

# Create your views here.
def index(request):
    return render(request, "api/index.html")


@api_view(['GET'])
def bike_parkings(request, distance=5):
    point = Point(-73.567256, 45.5016889)
    bike_parkings = BikeParking.objects.filter(position__distance_lte=(point, D(km=distance)))
    serializer = BikeParkingSerializer(bike_parkings, many=True)
    return Response(serializer.data)
