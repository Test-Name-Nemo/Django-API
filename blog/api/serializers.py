from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSer(serializers.ModelSerializers):
    class Meta:
        model = Measurement
        fields = '__all__'


class SensorSer(serializers.ModelSerializers):
    measurement = MeasurementSer(read_only=True, many=True)

    class Meta:
        model = Sensor
        field = ['id', 'name', 'desc', 'measurements']
