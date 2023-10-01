from rest_framework import serializers
from .models import PiValue


class PiValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiValue
        fields = "__all__"
