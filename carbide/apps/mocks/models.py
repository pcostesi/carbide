from django.db import models

# Create your models here.

class HelloModel(models.Model):
   description = models.TextField(blank=True)
   enabled = models.BooleanField(default=True)

