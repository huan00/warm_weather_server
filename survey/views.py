from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from weather.models import Weather
from user.models import User
from .models import Survey, Question
from weather.serializers import WeatherSerializer
from .serializers import SurveySerializer, QuestionSerializer, SurveyQuestionSerializer

# Create your views here.

class SurveyView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SurveySerializer
    survey_question_class = SurveyQuestionSerializer
    weather_serializer_class =  WeatherSerializer
    question_serializer_class = QuestionSerializer

    def post(self, request):
        date = request.data['date']
        user_id = request.data['user_id']
        weather = request.data['weather']

        user = User.objects.get(pk=user_id)
        
        # check if weather exist
        weather_exist = Weather.objects.get(weather_date=weather['weather_date'], zip_code=weather['zip_code'], location=weather['location'])
        if not weather_exist:
            weather_serializer = self.weather_serializer_class(data=weather)
            if weather_serializer.is_valid():
                weather = Weather.objects.create(weather)
        else:
            weather_serializer = WeatherSerializer(weather_exist)

        survey_data = {'survey_date': date, 'user_id':user_id, 'weather_id': weather_serializer.data['id']}
        survey_serializer = self.serializer_class(data=survey_data)

        if survey_serializer.is_valid(raise_exception=True):
            survey = self.create(survey_serializer)
            survey_id = Survey.objects.get(pk=survey.data['id'])

            question_data = request.data['question']
            question = Question.objects.create(**question_data, survey_id=survey_id)
            question.save()

        else:

            print(survey_serializer.errors)

        response_data = SurveyQuestionSerializer(survey_id)
        print(response_data.data)

        # return Response('hello')
        
        return Response(response_data.data)
    
@api_view(['GET'])
def get_survey(request, pk=None):
    survey = Survey.objects.get(pk=pk)
    print('hello')
    survey_serializer = SurveyQuestionSerializer(survey)
    print(survey_serializer.data)
    # return Response('hello')
    return Response(survey_serializer.data)


@api_view(['GET'])
def get_question(request,pk=None):
    question = Question.objects.get(pk=pk)
    question_serializer = QuestionSerializer(question)

    return Response(question_serializer.data)