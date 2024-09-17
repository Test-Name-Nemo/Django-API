from .models import Sensor, Measurement
from .serializers import SensorSer, MeasurementSer
from rest_framework import viewsets


class MeasurementsViewSet(viewsets.ModelviewSet):
    queryset = Measurement.ovject.all()
    serializer_class = MeasurementSer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer = SensorSer
