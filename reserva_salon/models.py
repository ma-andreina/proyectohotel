from django.db import models


class ReservaSalon(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField(null=True)
    salon_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'reserva_salon'
        managed = True

    def __str__(self):
        return str(self.id)
