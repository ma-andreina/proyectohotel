# restaurante_mesa/models.py

from django.db import models
from django.core.validators import MinValueValidator 

class RestauranteMesa(models.Model):
    
    # Definición de las opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('LIBRE', 'Libre'),
        ('OCUPADA', 'Ocupada'),
        ('RESERVADA', 'Reservada'),
        ('LIMPIEZA', 'Limpieza'),
    ]
    
    numero_mesa = models.IntegerField(unique=True) 
    
    capacidad = models.IntegerField(
        default=2, 
        validators=[MinValueValidator(1, message="La capacidad debe ser un entero positivo.")]
    )
    
    ubicacion = models.CharField(max_length=50, choices=[
        ('terraza', 'Terraza'),
        ('interior', 'Interior'),
    ])
    
    #  NUEVO CAMPO 1: Estado de disponibilidad inmediata
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='LIBRE',
        help_text="Disponibilidad inmediata: Libre, Ocupada, Reservada, Limpieza."
    )
    
    #  NUEVO CAMPO 2: Estado operativo (activa)
    activa = models.BooleanField(
        default=True,
        help_text="Indica si la mesa está disponible para el sistema (True) o fuera de servicio (False)."
    )
    
    class Meta:
        db_table = 'restaurante_mesa' 
        verbose_name = 'Mesa de Restaurante'

    def __str__(self):
        return f"Mesa {self.numero_mesa} ({self.capacidad}p) - {self.estado}"