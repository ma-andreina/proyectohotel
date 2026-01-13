from rest_framework import serializers
from .models import ReservaSalon
from django.utils import timezone

class ReservaSalonSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ReservaSalon.
    Maneja la visualización de datos relacionados y protege campos generados por el sistema.
    """
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    nombre_salon = serializers.CharField(source='salon.nombre', read_only=True)

    class Meta:
        model = ReservaSalon
        fields = [
            'id', 'usuario', 'usuario_username', 'salon', 'nombre_salon', 
            'fecha_evento', 'cantidad_invitados', 'codigo_evento', 
            'estado', 'total_reserva', 'fecha_creacion'
        ]
        # Estos campos son gestionados por el modelo o la vista, no por el cliente
        read_only_fields = ['usuario', 'codigo_evento', 'total_reserva', 'fecha_creacion']

    def validate_fecha_evento(self, value):
        """
        Valida que la fecha del evento no sea en el pasado.
        """
        if value < timezone.now():
            raise serializers.ValidationError("La fecha del evento no puede ser en el pasado.")
        return value

    def validate_cantidad_invitados(self, value):
        """
        Valida que la cantidad de invitados sea razonable (al menos 1).
        """
        if value <= 0:
            raise serializers.ValidationError("El número de invitados debe ser al menos 1.")
        return value