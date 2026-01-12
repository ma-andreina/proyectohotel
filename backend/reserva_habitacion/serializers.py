# reserva_habitacion/serializers.py

from rest_framework import serializers
from .models import ReservaHabitacion
from habitacion.models import Habitacion 
from django.utils import timezone 
from django.db.models import Q 

class ReservaHabitacionSerializer(serializers.ModelSerializer):
    
    usuario_username = serializers.CharField(source='usuario.username', read_only=True) 
    numero_habitacion = serializers.CharField(source='habitacion.numero_habitacion', read_only=True)
    
    class Meta:
        model = ReservaHabitacion
        fields = '__all__'
        read_only_fields = ['codigo_confirmacion', 'fecha_creacion']

    def validate(self, data):
        """
        Implementa las validaciones de negocio para la reserva.
        """
        fecha_checkin = data.get('fecha_checkin')
        fecha_checkout = data.get('fecha_checkout')
        habitacion = data.get('habitacion')
        
        
        # OBTENCIÓN DE FECHA ACTUAL (CORRECCIÓN CRÍTICA PARA TIMEZONES):
        today = timezone.localdate() 
        today_str = today.isoformat()
        fecha_checkin_str = fecha_checkin.isoformat() 

        # =========================================================
        # 1. RESTRICCIÓN: No Fecha Anterior a la Actual
        # =========================================================
        if fecha_checkin_str < today_str:
             raise serializers.ValidationError({'fecha_checkin': 'No se puede reservar una habitación con fecha anterior a la actual.'})

        # Validación: Check-out debe ser posterior al Check-in
        if fecha_checkin >= fecha_checkout:
            raise serializers.ValidationError({'fecha_checkout': 'El check-out debe ser posterior al check-in.'})
            
        # =========================================================
        # 2. RESTRICCIÓN: Solo Habitación con Estado Disponible
        # =========================================================
        if habitacion.estado != Habitacion.ESTADO_DISPONIBLE:
             raise serializers.ValidationError({
                'habitacion': f'La habitación {habitacion.numero_habitacion} no está disponible. Su estado actual es: {habitacion.get_estado_display()}.'
            })

        # =========================================================
        # 3. VALIDACIÓN DE DISPONIBILIDAD (Superposición)
        # =========================================================
        superpuestas = ReservaHabitacion.objects.filter(
            habitacion=habitacion,
            fecha_checkin__lt=fecha_checkout, 
            fecha_checkout__gt=fecha_checkin,
            # Solo se consideran conflictos PENDIENTE o CONFIRMADA
            estado__in=[ReservaHabitacion.ESTADO_PENDIENTE, ReservaHabitacion.ESTADO_CONFIRMADA] 
        )
        
        if self.instance: 
            superpuestas = superpuestas.exclude(pk=self.instance.pk)

        if superpuestas.exists():
            raise serializers.ValidationError({
                'habitacion': f'Habitación {habitacion.numero_habitacion} no disponible en ese rango de fechas.'
            })

        return data