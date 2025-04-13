from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    value = models.FloatField(blank=True, null=True)
    command = models.CharField(max_length=100, blank=True, null=True)

    def get_value(self):
        from .views import arduino
        if self.command:
            res = arduino.send_command(self.command)
            self.value = float(res)
        return self.value

    def __str__(self):
        return self.name

class Mechanism(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    max_value = models.FloatField(blank=True, null=True)
    min_value = models.FloatField(blank=True, null=True)

    status = models.BooleanField(default=False)

    normal_value = models.FloatField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    command = models.CharField(max_length=100, blank=True, null=True)

    def on(self):
        from .views import arduino
        if self.command:
            arduino.send_command(self.command + " on")
            
    def off(self):
        from .views import arduino
        if self.command:
            arduino.send_command(self.command + " off")
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name