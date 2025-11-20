from django.db import models


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.TextField(unique=True, null=True)
    nombre = models.TextField(null=True)
    apellido = models.TextField(null=True)

    class Meta:
        db_table = 'usuario'
        managed = True

    def __str__(self):
        return self.email or str(self.id)
