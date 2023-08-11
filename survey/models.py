from django.db import models
from weather.models import Weather

# Create your models here.


class Survey(models.Model):
    # survey_question = models.CharField(max_length=255)
    survey_date = models.CharField(max_length=50)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    weather_id = models.ForeignKey(Weather, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.survey_date)


class Questions(models.Model):
    survey_question = models.CharField(max_length=255)
    survey_answer = models.CharField(max_length=255)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.survey_question
