# habitacion/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Habitacion
from .serializers import HabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet simple para gestionar habitaciones
    """
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    
    def get_queryset(self):
        """
        Filtros simples por parámetros URL
        """
        queryset = Habitacion.objects.all()
        
        # Filtro por estado
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        
        # Filtro por piso
        piso = self.request.query_params.get('piso')
        if piso:
            queryset = queryset.filter(piso=piso)
        
        # Filtro por categoría
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        
        # Filtro por tipo de ocupación
        tipo_ocupacion = self.request.query_params.get('tipo_ocupacion')
        if tipo_ocupacion:
            queryset = queryset.filter(tipo_ocupacion=tipo_ocupacion)
        
        # Filtro por precio máximo
        precio_max = self.request.query_params.get('precio_max')
        if precio_max:
            queryset = queryset.filter(precio_base__lte=precio_max)
        
        # Filtro por precio mínimo
        precio_min = self.request.query_params.get('precio_min')
        if precio_min:
            queryset = queryset.filter(precio_base__gte=precio_min)
        
        # Solo habitaciones activas por defecto
        mostrar_inactivas = self.request.query_params.get('mostrar_inactivas')
        if not mostrar_inactivas:
            queryset = queryset.filter(activa=True)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        """
        Endpoint simple para habitaciones disponibles
        """
        habitaciones = Habitacion.objects.filter(
            estado=Habitacion.ESTADO_DISPONIBLE,
            activa=True
        )
        
        # Aplicar filtros adicionales si existen
        categoria = request.query_params.get('categoria')
        if categoria:
            habitaciones = habitaciones.filter(categoria=categoria)
        
        tipo_ocupacion = request.query_params.get('tipo_ocupacion')
        if tipo_ocupacion:
            habitaciones = habitaciones.filter(tipo_ocupacion=tipo_ocupacion)
        
        precio_max = request.query_params.get('precio_max')
        if precio_max:
            habitaciones = habitaciones.filter(precio_base__lte=precio_max)
        
        serializer = self.get_serializer(habitaciones, many=True)
        return Response({
            'total': habitaciones.count(),
            'habitaciones': serializer.data
        })
    
    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        """
        Cambiar estado de una habitación
        """
        habitacion = self.get_object()
        nuevo_estado = request.data.get('estado')
        
        # Validar que el estado sea válido
        estados_validos = [choice[0] for choice in Habitacion.ESTADO_CHOICES]
        if nuevo_estado not in estados_validos:
            return Response(
                {'error': f'Estado no válido. Estados permitidos: {estados_validos}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        habitacion.estado = nuevo_estado
        habitacion.save()
        
        serializer = self.get_serializer(habitacion)
        return Response(serializer.data)