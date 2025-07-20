from django.db import models
from django.utils import timezone

class PromptResponseLog(models.Model):
    action_type = models.CharField(max_length=100)
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.action_type} @ {self.created_at.strftime('%Y-%m-%d %H:%M')}"
