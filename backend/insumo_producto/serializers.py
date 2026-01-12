from rest_framework import serializers
from .models import InsumoProducto
from django.utils import timezone

class InsumoProductoSerializer(serializers.ModelSerializer):
    # Campo calculado para saber si está vencido
    esta_vencido = serializers.SerializerMethodField()
    
    class Meta:
        model = InsumoProducto
        fields = '__all__'
        read_only_fields = ('id',)
    
    def get_esta_vencido(self, obj):
        if obj.fecha_vencimiento:
            return obj.fecha_vencimiento < timezone.now().date()
        return False
    
    def validate(self, data):
        # Validar que el stock actual no sea negativo
        if 'stock_actual' in data and data['stock_actual'] < 0:
            raise serializers.ValidationError({
                'stock_actual': 'El stock actual no puede ser negativo.'
            })
        
        # Validar que el costo de venta sea mayor o igual al costo de compra
        if 'costo_compra' in data and 'costo_venta' in data:
            if data['costo_venta'] < data['costo_compra']:
                raise serializers.ValidationError({
                    'costo_venta': 'El costo de venta no puede ser menor al costo de compra.'
                })
        
        # Validar fecha de vencimiento
        if 'fecha_vencimiento' in data and data['fecha_vencimiento']:
            if data['fecha_vencimiento'] < timezone.now().date():
                raise serializers.ValidationError({
                    'fecha_vencimiento': 'La fecha de vencimiento no puede ser en el pasado.'
                })
        
        return data