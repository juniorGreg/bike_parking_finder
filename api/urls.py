from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('confirm_email', views.confirm_email, name="confirm_email"),
    path("api/bike_parkings", views.bike_parkings, name="api")
]
