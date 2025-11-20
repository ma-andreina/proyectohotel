from django.db import models


class ReservaRestaurante(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField(null=True)
    mesa_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'reserva_restaurante'
        managed = True

    def __str__(self):
        return str(self.id)
