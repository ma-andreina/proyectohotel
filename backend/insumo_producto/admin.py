from django.contrib import admin
from django.utils.html import format_html
from .models import InsumoProducto
from django.utils import timezone

@admin.register(InsumoProducto)
class InsumoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock_actual', 'stock_inicial', 
                    'costo_compra', 'costo_venta', 'estado', 
                    'fecha_vencimiento', 'verificar_vencimiento_admin')
    list_filter = ('estado', 'marca', 'color')
    search_fields = ('nombre', 'marca', 'description')
    list_editable = ('stock_actual', 'estado')
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'description', 'estado')
        }),
        ('Stock y Costos', {
            'fields': ('stock_inicial', 'stock_actual', 'costo_compra', 'costo_venta')
        }),
        ('Características', {
            'fields': ('marca', 'color', 'fecha_vencimiento')
        }),
    )
    
    def verificar_vencimiento_admin(self, obj):
        from django.utils import timezone
        if obj.fecha_vencimiento:
            if obj.fecha_vencimiento < timezone.now().date():
                return format_html('<span style="color: red;">VENCIDO</span>')
            elif (obj.fecha_vencimiento - timezone.now().date()).days <= 30:
                return format_html('<span style="color: orange;">Próximo a vencer</span>')
            else:
                return format_html('<span style="color: green;">Vigente</span>')
        return 'Sin fecha'
    
    verificar_vencimiento_admin.short_description = 'Estado Vencimiento'
    
    # Acción personalizada para marcar como activo/inactivo
    actions = ['marcar_como_activo', 'marcar_como_inactivo']
    
    def marcar_como_activo(self, request, queryset):
        updated = queryset.update(estado='activo')
        self.message_user(request, f'{updated} productos marcados como activos.')
    
    def marcar_como_inactivo(self, request, queryset):
        updated = queryset.update(estado='inactivo')
        self.message_user(request, f'{updated} productos marcados como inactivos.')
    
    marcar_como_activo.short_description = "Marcar como activo"
    marcar_como_inactivo.short_description = "Marcar como inactivo"