from rest_framework import serializers
from .models import Survey, Question
from user.models import User
from weather.models import Weather
from weather.serializers import WeatherSerializer
from rest_framework.response import Response

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = (
            'id',
            'survey_date',
            'user_id',
        )
    
    def create(self, validated_data):
        survey = Survey.objects.create(**validated_data)
        return survey


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'survey_date', 'survey_question', 'survey_answer')


        def create(self, validated_data):
            return super(QuestionSerializer, self).create(validated_data)

class SurveyQuestionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username')
    weather = WeatherSerializer('weather')
    
    class Meta:
        model = Survey
        fields = ('id', 'survey_date','username', 'questions', 'weather')
