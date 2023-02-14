from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeatherData(models.Model):
    city_name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    icon=models.CharField(max_length=200)
    temperature = models.FloatField()
    humidity = models.FloatField()