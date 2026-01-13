# reserva_habitacion/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaHabitacionViewSet

# Creamos el router de Django Rest Framework
router = DefaultRouter()

# Registramos el ViewSet. 
# Al usar 'reservas', la URL final será: /api/reservas-habitacion/reservas/
router.register(r'reservas', ReservaHabitacionViewSet, basename='reserva-habitacion')

urlpatterns = [
    # Incluimos las rutas generadas automáticamente por el router
    path('', include(router.urls)),
]