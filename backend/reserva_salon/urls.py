from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaSalonViewSet

router = DefaultRouter()
router.register(r'reservas', ReservaSalonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]