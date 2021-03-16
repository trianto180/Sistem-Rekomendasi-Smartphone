from django.db import models
from datetime import datetime

# Create your models here.
class Smartphone(models.Model):
    model = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    cpu_spek = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    storage_rem = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    launcher = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    recharge = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)
    facial = models.CharField(max_length=255)

    def __str__(self):
        return self.model

class smartphone_recomm(models.Model):
    smartphone_name=models.CharField(max_length=256)
    ram = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    cos_sim=models.FloatField(null=False)

    def __str__(self):
        return self.smartphone_name
