from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatoViewSet

router = DefaultRouter()
router.register(r'platos', PlatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]