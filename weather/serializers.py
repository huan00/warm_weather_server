from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.Serializer):

    # date = serializers.DateField()
    # temperature = serializers.CharField(max_length=50)
    # wind = serializers.CharField(max_length=50)
    # condition = serializers.CharField(max_length=50)
    # feels_like = serializers.CharField(max_length=50)
    # humidity = serializers.CharField(max_length=50)

    class Meta:
        model = Weather
        fields = '__all__'
