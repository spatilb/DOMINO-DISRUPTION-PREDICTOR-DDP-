from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class DisruptionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    duration = models.IntegerField() # Duration in minutes
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    context = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp} - {self.tag.name if self.tag else 'No Tag'}"

class RootCauseRule(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    root_cause_label = models.CharField(max_length=255)

    def __str__(self):
        return f"Rule: {self.tag.name} + '{self.keyword}' -> {self.root_cause_label}"

class SuggestionTemplate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    template_text = models.TextField()

    def __str__(self):
        return self.name
