# salon_eventos/views.py

from rest_framework import viewsets
from .models import SalonEvento
from .serializers import SalonEventoSerializer

class SalonEventoViewSet(viewsets.ModelViewSet):
    """
    API para la gestión completa de los Salones de Eventos (CRUD).
    """
    queryset = SalonEvento.objects.all().order_by('nombre')
    serializer_class = SalonEventoSerializer
    # Se pueden agregar permisos aquí