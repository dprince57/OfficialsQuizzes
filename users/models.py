from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('official', 'Official'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='official')
    sport = models.CharField(max_length=50, null=True, blank=True)  # e.g., NCAA Football
