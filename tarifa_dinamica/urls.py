from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarifaDinamicaViewSet

router = DefaultRouter()
router.register(r'tarifas', TarifaDinamicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]