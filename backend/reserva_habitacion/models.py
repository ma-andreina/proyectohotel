from django.db import models


class ReservaHabitacion(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField(null=True)
    habitacion_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'reserva_habitacion'
        managed = True

    def __str__(self):
        return str(self.id)
