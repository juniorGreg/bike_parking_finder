from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class BikeParking(models.Model):
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=400)
    capacity = models.PositiveIntegerField(default=1)
    indoor = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    position = models.PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.position, 'coords', [])[::-1])

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    added_bike_parkings = models.ManyToManyField(BikeParking, related_name="added_bike_parking_set")
    modified_bike_parkings = models.ManyToManyField(BikeParking, related_name="modified_bike_parking_set")
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
