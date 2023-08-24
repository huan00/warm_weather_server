from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from user.models import User
from .models import Survey, Question

from .serializers import SurveySerializer, QuestionSerializer, SurveyDetailSerializer, WeatherSerializer, ClothingSerializer

# Create your views here.

class SurveyView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SurveySerializer
    survey_detail_class = SurveyDetailSerializer
    question_serializer_class = QuestionSerializer
    weather_serializer_class = WeatherSerializer
    clothing_serializer_class = ClothingSerializer

    def post(self, request):
        date = request.data['date']
        user = request.data['user']
        question_data = request.data['question']
        clothing_data = request.data['clothing']
        weather_data = request.data['weather']
        survey_data = {'survey_date':date, 'user':user}

        try:
            survey_exists = Survey.objects.filter(**survey_data).exists()
            if survey_exists:
                return Response('Survey already exists')
            
            survey_serializer = self.serializer_class(data=survey_data)

            # create survey after checking data
            if survey_serializer.is_valid(raise_exception=True):
                survey=self.create(survey_serializer)

                # create questions
                question_serializer = QuestionSerializer(data={**question_data, 'survey':survey.data['id']})
                if question_serializer.is_valid(raise_exception=True):
                    question_serializer.save()

                # create weather
                weather_serializer = self.weather_serializer_class(data={**weather_data, 'survey_weather': survey.data['id']})
                if weather_serializer.is_valid(raise_exception=True):
                    weather_serializer.save()
                #create clothing
                clothing_serializer = self.clothing_serializer_class(data={**clothing_data, 'survey_clothing': survey.data['id']})
                if clothing_serializer.is_valid(raise_exception=True):
                    clothing_serializer.save()

                # pull data from survey, clothing, weather, and question for response
                survey_response = Survey.objects.get(pk=survey.data['id'])
                survey_response = SurveyDetailSerializer(survey_response)

                return Response(survey_response.data, status=status.HTTP_201_CREATED)
        except:
            # if error delete created survey.
            survey = Survey.objects.get(**survey_data)
            survey.delete()
            return Response({'msg': 'error creating survey'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_survey(request, pk=None):
    survey = Survey.objects.get(pk=pk)

    survey_serializer = SurveyDetailSerializer(survey)
    print(survey_serializer.data)

    return Response(survey_serializer.data)


@api_view(['GET'])
def get_question(request,pk=None):
    question = Question.objects.get(pk=pk)
    question_serializer = QuestionSerializer(question)

    return Response(question_serializer.data)