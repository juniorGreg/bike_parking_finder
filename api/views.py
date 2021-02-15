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
from django.http import StreamingHttpResponse

from allauth.socialaccount.models import SocialLogin
from time import sleep
import redis
import json

redis_client = redis.Redis(host="localhost", port=6379)


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


def event_heatmap():
    init_heatmap_data = redis_client.lrange("heatmap_data", 0, -1)
    yield "data: %s\n\n" % init_heatmap_data
    sub = redis_client.pubsub()
    sub.subscribe("heatmap")
    while True:
        update_heatmap = sub.get_message()
        if update_heatmap and not update_heatmap['data'] == 1:
            yield 'data: %s\n\n' % update_heatmap["data"].decode("utf-8")



def heatmap(request):
    response = StreamingHttpResponse(event_heatmap(), content_type='text/event-stream')
    return response


@api_view(['GET'])
def bike_parkings(request):
    distance = float(request.GET.get("radius", "5000"))
    lat = float(request.GET.get("lng", '45.5016889'))
    lng = float(request.GET.get("lat", "-73.567256"))
    point = Point(lat, lng)
    bike_parkings = BikeParking.objects.filter(position__distance_lte=(point, D(m=distance)))

    heatmap_data = [json.dumps(bike_parking.lat_lng) for bike_parking in bike_parkings]

    for bike_parking in heatmap_data:
        #print(bike_parking)
        redis_client.lpush("heatmap_data", bike_parking)
        redis_client.publish("heatmap", bike_parking)
        redis_client.ltrim("heatmap_data", 0, 999)


    serializer = BikeParkingSerializer(bike_parkings, many=True)
    return Response(serializer.data)

def confirm_email(request, key):
    context = {
        "key": key
    }
    return render(request, "api/email_confirmation.html", context)
