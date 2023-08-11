from django.db import models
from survey.models import Survey

# Create your models here.


class Weather(models.Model):
    date = models.CharField(max_length=50)
    temperature_high = models.CharField(max_length=50)
    temperature_low = models.CharField(max_length=50)
    temperature_avg = models.CharField(max_length=50)
    wind_mph = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    feels_like = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    zip_code = models.IntegerField(default=00000, blank=True)
    survey_id = models.OneToOneField(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
