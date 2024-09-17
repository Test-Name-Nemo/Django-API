from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, versobe_name='Нaзвание')
    models = models.CharField(max_length=100, versobe_name='Описание')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
