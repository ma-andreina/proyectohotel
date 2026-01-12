from django.db import models

class InsumoProducto(models.Model):
    # Estados posibles para el producto
    ESTADOS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('vencido', 'Vencido'),
    ]
    
    # Ya tienes estos campos, pero vamos a ajustarlos según la documentación
    id = models.AutoField(primary_key=True)  # Cambié a AutoField para autoincrement
    nombre = models.CharField(max_length=255)  # Cambié a CharField
    description = models.TextField(blank=True, null=True)  # Campo nuevo
    costo_compra = models.DecimalField(max_digits=10, decimal_places=2)  # Campo nuevo
    costo_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Campo nuevo
    stock_inicial = models.IntegerField(default=0)  # Campo nuevo
    stock_actual = models.IntegerField(default=0)
    marca = models.CharField(max_length=100, blank=True, null=True)  # Campo nuevo
    color = models.CharField(max_length=50, blank=True, null=True)  # Campo nuevo
    fecha_vencimiento = models.DateField(blank=True, null=True)  # Campo nuevo
    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='activo')  # Campo nuevo

    class Meta:
        db_table = 'insumo_producto'
        verbose_name = 'Insumo/Producto'
        verbose_name_plural = 'Insumos/Productos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock_actual})"
    
    # Método para verificar si el producto está vencido
    def verificar_vencimiento(self):
        from django.utils import timezone
        if self.fecha_vencimiento and self.fecha_vencimiento < timezone.now().date():
            self.estado = 'vencido'
            self.save()
        return self.estado == 'vencido'