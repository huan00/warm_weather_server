from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'
        # fields = (
        #         'id',
        #         'weather_date',
        #         'temperature_high',
        #         'temperature_low',
        #         'temperature_avg',
        #         'wind_mph',
        #         'condition',
        #         'feels_like',
        #         'humidity',
        #         'location',
        #         'zip_code',
        #         )

    def create(self, validated_data):
        return super(WeatherSerializer, self).create(validated_data)
        
