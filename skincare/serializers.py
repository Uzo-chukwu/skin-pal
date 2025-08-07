from rest_framework import serializers
from .models import SkinAnalysis, SkincareProgress
from .models import SkinProfile

class SkinAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinAnalysis
        fields = ['id', 'user', 'image', 'analysis_result', 'created_at']
        read_only_fields = ['id', 'user', 'analysis_result', 'created_at']


from .models import SkincareRoutine

class SkincareRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkincareRoutine
        fields = ['id', 'name', 'steps', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

from .models import SkincareReminder


class SkincareReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkincareReminder
        fields = '__all__'
        read_only_fields = ['user']


class SkincareProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkincareProgress
        fields = '__all__'
        read_only_fields = ['user', 'timestamp']


class SkinProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinProfile
        fields = ['skin_type', 'sensitivity', 'concerns']
