from rest_framework import viewsets
from .models import ReservaServicio
from .serializers import ReservaServicioSerializer

class ReservaServicioViewSet(viewsets.ModelViewSet):
    queryset = ReservaServicio.objects.all()
    serializer_class = ReservaServicioSerializer