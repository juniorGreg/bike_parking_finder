from django.contrib.gis.db import models

# Create your models here.
class BikeParking(models.Model):
    name = models.CharField(max_length=400)
    capacity = models.PositiveIntegerField(default=1)
    indoor = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, null=True)
    position = models.PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.position, 'coords', [])[::-1])

    def __str__(self):
        return self.name
