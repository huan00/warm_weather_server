from django.db import models
from user.models import User


# Create your models here.


class Survey(models.Model):
    survey_date = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='surveys', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    # acceptable question answer: [very cold, little cold, comfortable, hot, very hot]
    survey_date = models.CharField(max_length=50)
    survey_question = models.CharField(max_length=200)
    survey_answer = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Clothing(models.Model):
    hat = models.CharField(max_length=100, default='', blank=True)
    scarf = models.CharField(max_length=100, default='', blank=True)
    shirt = models.CharField(max_length=100, blank=False)
    jacket = models.CharField(max_length=100, default='', blank=True)
    pants = models.CharField(max_length=100, blank=False)
    shoes = models.CharField(max_length=100, blank=False)
    survey_clothing = models.OneToOneField(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    

class Weather(models.Model):
    survey_weather = models.OneToOneField(Survey, on_delete=models.CASCADE)
    weather_date = models.CharField(max_length=50)
    temperature_high = models.CharField(max_length=50)
    temperature_low = models.CharField(max_length=50)
    temperature_avg = models.CharField(max_length=50)
    wind_mph = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    feels_like = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)