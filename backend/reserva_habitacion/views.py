from rest_framework import viewsets
from .models import ReservaHabitacion
from .serializers import ReservaHabitacionSerializer

class ReservaHabitacionViewSet(viewsets.ModelViewSet):
    queryset = ReservaHabitacion.objects.all()
    serializer_class = ReservaHabitacionSerializer