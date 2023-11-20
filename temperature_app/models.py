from django.db import models
from timescale.db.models.models import TimescaleModel

class TemperatureReading(TimescaleModel):
    temperature = models.FloatField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.temperature} at {self.time}"
