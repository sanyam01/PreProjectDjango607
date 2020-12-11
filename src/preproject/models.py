from django.db import models
# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Create your models here.

class ProductField(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message