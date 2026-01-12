# salon_eventos/models.py

from django.db import models

class SalonEvento(models.Model):
    nombre = models.CharField(max_length=100) # [cite: 793]
    descripcion = models.TextField() # [cite: 793]
    capacidad = models.IntegerField() # [cite: 793]
    # Comodidades como proyector, sonido se pueden manejar con un campo TextField o un ManyToMany
    comodidades = models.TextField(help_text="Lista de comodidades (proyector, sonido, etc.)") # [cite: 793]
    precio_base_hora = models.DecimalField(max_digits=10, decimal_places=2) # [cite: 793]
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'salon_evento'
        verbose_name = 'Salón de Eventos'

    def __str__(self):
        return self.nombre
