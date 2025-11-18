from django.db import models


class Plato(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(null=True)
    precio = models.FloatField(null=True)

    class Meta:
        db_table = 'plato'
        managed = True

    def __str__(self):
        return self.nombre or str(self.id)
