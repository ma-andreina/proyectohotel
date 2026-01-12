# restaurante_mesa/views.py

from rest_framework import viewsets
from .models import RestauranteMesa
from .serializers import RestauranteMesaSerializer

# Usamos PascalCase para la clase (Convención de Clases) [cite: 456]
class RestauranteMesaViewSet(viewsets.ModelViewSet):
    """
    API para la gestión completa de las Mesas del Restaurante (CRUD).
    """
    queryset = RestauranteMesa.objects.all().order_by('numero_mesa')
    serializer_class = RestauranteMesaSerializer
    # Se pueden agregar permisos aquí (ej: solo Admin puede crear/modificar)