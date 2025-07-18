from rest_framework import serializers
from .models import SkinReport

class SkinReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinReport
        fields = '__all__'
        read_only_fields = ['result']