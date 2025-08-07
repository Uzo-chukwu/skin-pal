from django.db import models
from users.models import User
from django.conf import settings

class SkinAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="analyses")
    image = models.ImageField(upload_to='skin_uploads/')
    analysis_result = models.JSONField()  # We'll mock this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Skin analysis for {self.user.email} at {self.created_at}"

class SkincareRoutine(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='routines')
    name = models.CharField(max_length=100)
    steps = models.JSONField(default=list)  # List of {"step": "Cleanser", "time": "morning"}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.email}"




class SkincareReminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    routine = models.ForeignKey('SkincareRoutine', on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    note = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.routine.name} @ {self.time}"


class SkincareProgress(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='progress/')
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.timestamp.date()}"
class SkinProfile(models.Model):
    SKIN_TYPES = [
        ('Dry', 'Dry'),
        ('Oily', 'Oily'),
        ('Normal', 'Normal'),
        ('Combination', 'Combination'),
    ]

    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='skin_profile')
    skin_type = models.CharField(max_length=20, choices=SKIN_TYPES)
    sensitivity = models.BooleanField(default=False)
    concerns = models.TextField(help_text="List skin concerns like acne, dryness, etc.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Skin Profile"
