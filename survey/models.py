from django.db import models
from user.models import User
from weather.models import Weather

# Create your models here.


class Survey(models.Model):
    # survey_question = models.CharField(max_length=255)
    survey_date = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='surveys', on_delete=models.CASCADE)
    weather = models.ForeignKey(Weather, related_name='survey_weather', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.survey_date)
    
   


class Question(models.Model):
    survey_date = models.CharField(max_length=50)
    survey_question = models.CharField(max_length=200)
    survey_answer = models.CharField(max_length=200)
    survey_id = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.survey_question
