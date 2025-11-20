from django.db import models


class ReservaServicio(models.Model):
    id = models.IntegerField(primary_key=True)
    reserva_habitacion_id = models.IntegerField(null=True)
    servicio_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'reserva_servicio'
        managed = True

    def __str__(self):
        return str(self.id)
