from django.db import models
from django.contrib.auth.models import User

class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True)