# reserva_habitacion/models.py

from django.db import models
from django.contrib.auth.models import User 
from habitacion.models import Habitacion # Necesario para la FK
from decimal import Decimal
import uuid 
import datetime

# =========================================================
# MODELO ReservaHabitacion (Tabla reserva_habitacion)
# =========================================================

class ReservaHabitacion(models.Model):
    
    # 1. ESTADOS DE RESERVA (SOLO LOS SOLICITADOS)
    ESTADO_PENDIENTE = 'pendiente'
    ESTADO_CONFIRMADA = 'confirmada'
    ESTADO_CANCELADA = 'cancelada'
    ESTADO_COMPLETADA = 'completada' # Reemplaza a Check-Out

    ESTADO_CHOICES = [
        (ESTADO_PENDIENTE, 'Pendiente de Pago'),
        (ESTADO_CONFIRMADA, 'Confirmada'),
        (ESTADO_CANCELADA, 'Cancelada'),
        (ESTADO_COMPLETADA, 'Completada (Check-Out)'),
    ]

    # Relaciones
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='reservas_habitacion',
        verbose_name='Cliente'
    )
    habitacion = models.ForeignKey(
        Habitacion, 
        on_delete=models.RESTRICT,
        related_name='reservas',
        verbose_name='Habitación Reservada'
    )
    
    # Campos de Reserva
    fecha_checkin = models.DateField(verbose_name='Fecha Check-In')
    fecha_checkout = models.DateField(verbose_name='Fecha Check-Out')
    huespedes = models.PositiveSmallIntegerField(default=1, verbose_name='Número de Huéspedes')
    
    # Campos Administrativos
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES,
        default=ESTADO_PENDIENTE,
        verbose_name='Estado de la Reserva'
    )
    codigo_confirmacion = models.CharField(
        max_length=50, 
        unique=True, 
        blank=True,
        verbose_name='Código de Confirmación'
    )
    
    # Campos Financieros y de Tiempo
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        verbose_name='Total de la Reserva'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de Creación'
    )

    class Meta:
        db_table = 'reserva_habitacion'
        verbose_name = 'Reserva de Habitación'
        verbose_name_plural = 'Reservas de Habitaciones'
        ordering = ['fecha_checkin', 'estado']
        
    def __str__(self):
        return f'Reserva #{self.codigo_confirmacion} - {self.usuario.username}'

    def save(self, *args, **kwargs):
        if not self.codigo_confirmacion:
            self.codigo_confirmacion = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)