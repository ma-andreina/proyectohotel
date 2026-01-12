# reserva_habitacion/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaHabitacionViewSet

router = DefaultRouter()
router.register(r'habitacion/reservas', ReservaHabitacionViewSet, basename='reserva-habitacion')

urlpatterns = [
    path('', include(router.urls)),
]