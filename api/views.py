from django.shortcuts import render
from .models import BikeParking

# Create your views here.
def index(request):
    return render(request, "api/index.html")
