from django.db import models


class ServicioAdicional(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(null=True)
    precio = models.FloatField(null=True)

    class Meta:
        db_table = 'servicio_adicional'
        managed = True

    def __str__(self):
        return self.nombre or str(self.id)
