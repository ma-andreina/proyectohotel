from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaSalonViewSet

# Creamos el router de Django Rest Framework para gestionar las rutas automáticamente
router = DefaultRouter()

# Registramos el ViewSet de Reservas de Salón.
# Al usar r'reservas' y el basename 'reserva-salon', las rutas finales serán:
# /api/reservas-salon/reservas/ (Listar y Crear)
# /api/reservas-salon/reservas/{id}/ (Detalle, Editar, Eliminar)
router.register(r'reservas', ReservaSalonViewSet, basename='reserva-salon')

urlpatterns = [
    # Incluimos las rutas generadas por el router (GET, POST, PUT, DELETE, etc.)
    path('', include(router.urls)),
]