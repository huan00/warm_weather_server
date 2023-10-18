from rest_framework import serializers
from .models import Prompts

class PromptsSerializer(serializers.ModelSerializer):

  class Meta:
      model = Prompts
      fields = ( 'User', 'gender', 'sensitivity_to_cold')

      def create(self, validated_data):
        return super(PromptsSerializer, self).create(validated_data)