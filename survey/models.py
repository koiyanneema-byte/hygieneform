from django.db import models

class HygieneSurvey(models.Model):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
        ('prefer_not', 'Prefer not to say'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    school = models.CharField(max_length=150)
    challenges = models.TextField()
    suggestions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.school})"