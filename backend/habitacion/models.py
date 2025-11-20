from django.db import models


class Habitacion(models.Model):
    id = models.IntegerField(primary_key=True)
    numero_habitacion = models.TextField(null=True)
    categoria = models.TextField(null=True)

    class Meta:
        db_table = 'habitacion'
        managed = True

    def __str__(self):
        return self.numero_habitacion or str(self.id)
