# proyectohotel-backend/usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegistroUsuarioAPIView # <-- Asegúrate de importar RegistroUsuarioAPIView

# 1. Router para ViewSet (CRUD de usuarios, probablemente para Administradores)
router = DefaultRouter()
router.register(r'gestion', UsuarioViewSet, basename='usuarios-gestion') # Cambié a 'gestion' para ser más claro.

urlpatterns = [
    # 2. Rutas generadas por el Router (ej: /api/usuarios/gestion/, /api/usuarios/gestion/1/)
    path('', include(router.urls)), 
    
    # 3. Ruta Específica para el REGISTRO (US-001)
    # Este endpoint NO usa autenticación y maneja la creación inicial del cliente.
    # Endpoint completo será: /api/usuarios/registro/
    path('registro/', RegistroUsuarioAPIView.as_view(), name='registro'),
]
