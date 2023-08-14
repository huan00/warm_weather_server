from rest_framework import serializers
from .models import Survey, Question

class SurveySerializer(serializers.Serializer):
    
    class Meta:
        model = Survey
        fields = '__all__'


class QuestionSerializer(serializers.Serializer):
    
    class Meta:
        model = Question
        fields = '__all__'