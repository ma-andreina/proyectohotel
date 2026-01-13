"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. ADMINISTRACIÓN
    path('admin/', admin.site.urls),
    
    # 2. SISTEMA DE RESERVAS (CON INTEGRACIÓN DE CELERY)
    # Estas rutas activan las tareas asíncronas de envío de correos
    path('api/reservas-habitacion/', include('reserva_habitacion.urls')),
    path('api/reservas-restaurante/', include('reserva_restaurante.urls')),
    path('api/reservas-salon/', include('reserva_salon.urls')),

    # 3. MÓDULOS DE USUARIOS Y HABITACIONES
    path('api/usuarios/', include('usuarios.urls')),
    path('api/habitaciones/', include('habitacion.urls')),

    # 4. GESTIÓN DE RESTAURANTE (MAESTROS)
    path('api/mesas-restaurante/', include('restaurante_mesa.urls')),
    path('api/menus-restaurante/', include('menu_restaurante.urls')),
    path('api/platos/', include('plato.urls')),
    path('api/menu-platos/', include('menu_plato.urls')),
    
    # 5. EVENTOS Y LOGÍSTICA
    path('api/salones-eventos/', include('salon_eventos.urls')),
    path('api/tarifas-dinamicas/', include('tarifa_dinamica.urls')),
    path('api/insumos-productos/', include('insumo_producto.urls')),

    # 6. OTROS SERVICIOS Y ATENCIÓN AL CLIENTE
    path('api/servicios-adicionales/', include('servicio_adicional.urls')),
    path('api/reservas-servicios/', include('reserva_servicio.urls')),
    path('api/atencion-cliente/', include('atencion_cliente.urls')),
]