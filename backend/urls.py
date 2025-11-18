"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/habitaciones/', include('habitacion.urls')),
    path('api/usuarios/', include('usuarios.urls')),
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
