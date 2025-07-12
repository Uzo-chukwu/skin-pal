from rest_framework import serializers

from reminders.serializers import ReminderSerializer
from .models import Routine

class RoutineSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = ['id', 'name', 'description', 'steps', 'frequency', 'reminders']
