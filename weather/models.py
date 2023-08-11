from django.db import models

# Create your models here.


class Weather(models.Model):
    date = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    wind = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    feels_like = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(default=00000, blank=True)

    def __str__(self):
        return str(self.date)
