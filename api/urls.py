from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("api/bike_parkings/<int:distance>", views.bike_parkings, name="api")
]
