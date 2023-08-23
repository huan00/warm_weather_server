from django.db import models
# from survey.models import Survey

# Create your models here.


class Weather(models.Model):
    weather_date = models.CharField(max_length=50)
    temperature_high = models.CharField(max_length=50)
    temperature_low = models.CharField(max_length=50)
    temperature_avg = models.CharField(max_length=50)
    wind_mph = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    feels_like = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=False)
    zip_code = models.IntegerField(blank=False)



    def __str__(self):
        return str(self.id)
