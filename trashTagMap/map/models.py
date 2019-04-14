from django.db import models


# Create your models here.
class TrashTag(models.Model):
    latitude = models.FloatField
    longitude = models.FloatField
    url = models.CharField(max_length=200)
