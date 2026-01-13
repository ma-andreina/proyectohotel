# proyectohotel-backend/usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importamos los nombres de clase correctos implementados en views.py
from .views import UserViewSet, PerfilViewSet, RegisterUserView 

# 1. Router para ViewSets (Gestión CRUD Protegida)
router = DefaultRouter()
# Gestión de Usuarios: URL base /api/usuarios/gestion/
router.register(r'gestion', UserViewSet, basename='usuarios-gestion') 
# Gestión de Perfiles: URL base /api/usuarios/perfiles/
router.register(r'perfiles', PerfilViewSet, basename='perfiles') 

urlpatterns = [
    # 2. Ruta Específica para el REGISTRO (US-001) - Abierta
    # URL completa: /api/usuarios/registro/
    path('registro/', RegisterUserView.as_view(), name='registro'),
    
    # 3. Rutas generadas por el Router (gestion y perfiles)
    path('', include(router.urls)), 
]
