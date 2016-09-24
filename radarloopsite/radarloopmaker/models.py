from django.db import models

from .get_radar_images import get_radar_images

class RadarInfo(models.Model):
    radarID = models.CharField(max_length=6)
    location = models.CharField(max_length=50)
    range = models.IntegerField()
    refresh_rate = models.IntegerField()

    def __str__(self):
        return self.radarID

    @classmethod
    def InitialiseDB(cls):
        RadarInfo.objects.all().delete()
        for radarID, details in get_radar_images.get_radar_details().items():
            RadarInfo(
                radarID=radarID, location=details['location'], range=details['range'],
                refresh_rate=details['refresh_rate']
            ).save()