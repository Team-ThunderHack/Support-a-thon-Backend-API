from rest_framework import serializers
from .models import Analysis

class AnalysisDetails(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields="__all__"