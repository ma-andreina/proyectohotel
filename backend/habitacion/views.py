from rest_framework import viewsets
from .models import Habitacion
from .serializers import HabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar habitaciones.
    
    Proporciona operaciones CRUD completas para las habitaciones
    e incluye filtros personalizados para una mejor organización
    y búsqueda de habitaciones.
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    
    def get_queryset(self):
        """
        Filtra las habitaciones por estado, piso y categoría.
        
        Los filtros se aplican mediante parámetros de consulta en la URL:
        - estado: Filtra por estado de la habitación
        - piso: Filtra por número de piso
        - categoria: Filtra por categoría de habitación
        
        Returns:
            QuerySet: Conjunto de habitaciones filtradas según los parámetros
        """
        queryset = Habitacion.objects.all()
        estado = self.request.query_params.get('estado')
        piso = self.request.query_params.get('piso')
        categoria = self.request.query_params.get('categoria')
        
        # Aplicar filtros solo si los parámetros están presentes
        # Esto evita filtros vacíos que podrían afectar el rendimiento
        if estado:
            queryset = queryset.filter(estado=estado)
        if piso:
            queryset = queryset.filter(piso=piso)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
            
        return queryset