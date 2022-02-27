from rest_framework import serializers
from preschool_app import models

class PreschoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.preschool
        fields="__all__"