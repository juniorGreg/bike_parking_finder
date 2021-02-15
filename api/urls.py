from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('callback/google', views.google_callback, name="google_callback"),
    path('callback/facebook', views.facebook_callback, name="facebook_callback"),
    path('heatmap', views.heatmap, name="heatmap"),
    path("api/bike_parkings", views.bike_parkings, name="api")
]
