# proyectohotel-backend/backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Ruta del Panel de Administración de Django
    path('admin/', admin.site.urls),
    
    # ------------------------------------------------------------------
    # RUTAS DE AUTENTICACIÓN (LOGIN/TOKENS) - US-002
    # ------------------------------------------------------------------
    
    # 1. Endpoint de LOGIN: Envías (username, password) y recibes (access token, refresh token)
    # Requisito: NF-010 (uso de JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 2. Endpoint de REFRESH: Envías el refresh token y recibes un nuevo access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ------------------------------------------------------------------
    # RUTAS DE LAS APPS LOCALES
    # ------------------------------------------------------------------
    
    # Ruta de  app de usuarios (donde irá el Registro US-001 y gestión de perfiles)
    path('api/usuarios/', include('usuarios.urls')), 
    
    # otras rutas existentes:
    path('api/habitaciones/', include('habitacion.urls')),
    path('api/reservas-habitacion/', include('reserva_habitacion.urls')),
    path('api/atencion-cliente/', include('atencion_cliente.urls')),
    path('api/servicios-adicionales/', include('servicio_adicional.urls')),
    path('api/reservas-restaurante/', include('reserva_restaurante.urls')),
    path('api/menus-restaurante/', include('menu_restaurante.urls')),
    path('api/platos/', include('plato.urls')),
    path('api/menu-platos/', include('menu_plato.urls')),
    path('api/mesas-restaurante/', include('restaurante_mesa.urls')),
    path('api/salones-eventos/', include('salon_eventos.urls')),
    path('api/reservas-salon/', include('reserva_salon.urls')),
    path('api/reservas-servicios/', include('reserva_servicio.urls')),
    path('api/tarifas-dinamicas/', include('tarifa_dinamica.urls')),
    path('api/insumos-productos/', include('insumo_producto.urls')),
]