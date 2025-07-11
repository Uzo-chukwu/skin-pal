from django.db import models
from routines.models import Routine

class Reminder(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='reminders')
    time_of_day = models.TimeField()
    message = models.CharField(max_length=255)
    repeat = models.CharField(max_length=20, choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='daily')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.routine.name} at {self.time_of_day}"
