from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaServicioViewSet

router = DefaultRouter()
router.register(r'reservas-servicios', ReservaServicioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]