from rest_framework import serializers
from .models import TemperatureReading


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = "__all__"