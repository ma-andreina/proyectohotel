from rest_framework import serializers
from .models import ReservaRestaurante

class ReservaRestauranteSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ReservaRestaurante.
    Se ha eliminado 'total_reserva' de los campos para simplificar la interfaz,
    ya que las reservas de mesa no requieren mostrar un costo.
    """
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    numero_mesa = serializers.CharField(source='mesa.numero_mesa', read_only=True)

    class Meta:
        model = ReservaRestaurante
        fields = [
            'id', 'usuario', 'usuario_username', 'mesa', 'numero_mesa', 
            'fecha_reserva', 'cantidad_personas', 'codigo_reserva', 
            'estado', 'notas', 'fecha_creacion'
        ]
        # Estos campos son gestionados por el sistema y no por el cliente
        read_only_fields = ['usuario', 'codigo_reserva', 'fecha_creacion']

    def validate_cantidad_personas(self, value):
        """
        Valida que la cantidad de personas sea al menos 1.
        """
        if value <= 0:
            raise serializers.ValidationError("La cantidad de personas debe ser al menos 1.")
        return value