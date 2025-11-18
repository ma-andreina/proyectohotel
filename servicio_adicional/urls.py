from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicioAdicionalViewSet

router = DefaultRouter()
router.register(r'servicios', ServicioAdicionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]