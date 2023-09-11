from rest_framework import serializers
from .models import Survey, Question, Clothing, Weather

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = (
            'id',
            'survey_date',
            'user',
        )
    
    def create(self, validated_data):
            return super(SurveySerializer, self).create(validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'survey_date', 'survey_question', 'survey_answer',
                  'survey')

        def create(self, validated_data):
            print('create question')
            return super(QuestionSerializer, self).create(validated_data)




class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'weather_date',
            'temperature_high',
            'temperature_low',
            'temperature_avg',
            'wind_mph',
            'condition',
            'feels_like',
            'humidity',
            'survey_weather'
        )
    

class ClothingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clothing
        fields = (
            'id',
            'hat',
            'scarf',
            'shirt',
            'jacket',
            'pants',
            'shoes',
            'survey_clothing'
        )

class UserSurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    clothing = ClothingSerializer(read_only=True)
    weather = WeatherSerializer(read_only=True)

    class Meta:
        model = Survey
        fields=('survey_date','questions','clothing','weather')



class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    clothing = ClothingSerializer(read_only=True)
    weather = WeatherSerializer(read_only=True)
    username = serializers.CharField(source='user.username')
    
    class Meta:
        model = Survey
        fields = ('id', 'survey_date','username', 'questions', 'clothing', 'weather')