from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaHabitacionViewSet

router = DefaultRouter()
router.register(r'reservas', ReservaHabitacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]