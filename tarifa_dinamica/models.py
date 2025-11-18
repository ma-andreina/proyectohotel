from django.db import models


class TarifaDinamica(models.Model):
    id = models.IntegerField(primary_key=True)
    habitacion_id = models.IntegerField(null=True)
    precio = models.FloatField(null=True)

    class Meta:
        db_table = 'tarifa_dinamica'
        managed = True

    def __str__(self):
        return str(self.id)
