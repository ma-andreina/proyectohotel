from django.db import models


class RestauranteMesa(models.Model):
    id = models.IntegerField(primary_key=True)
    numero_mesa = models.TextField(null=True)
    capacidad = models.IntegerField(null=True)

    class Meta:
        db_table = 'restaurante_mesa'
        managed = True

    def __str__(self):
        return self.numero_mesa or str(self.id)
