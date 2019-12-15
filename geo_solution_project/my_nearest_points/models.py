
from django.contrib.gis.db import models

# Create your models here.

class Points(models.Model):
    x = models.DecimalField(max_digits=10, decimal_places=2)
    y = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.AutoField(primary_key=True)
    location = models.PointField(srid=3857)
