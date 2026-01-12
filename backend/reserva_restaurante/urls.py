from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaRestauranteViewSet

router = DefaultRouter()
router.register(r'reservas', ReservaRestauranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]