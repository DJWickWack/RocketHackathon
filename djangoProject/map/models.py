from django.db import models


# Create your models here.
class TrashTag(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    url = models.CharField(max_length=150)

    def as_json(self):
        return dict(
            latitude=self.latitude,
            longitude=self.longitude,
            url=self.url
        )
