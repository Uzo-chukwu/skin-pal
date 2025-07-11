from django.db import models

class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    steps = models.TextField(help_text="List steps as comma-separated text")
    frequency = models.CharField(max_length=20, default='daily')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
