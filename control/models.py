from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Mechanism(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    max_value = models.FloatField(blank=True, null=True)
    min_value = models.FloatField(blank=True, null=True)

    status = models.BooleanField(default=False)

    normal_value = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return self.name