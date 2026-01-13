# proyectohotel-backend/usuarios/views.py
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView # Para un registro más limpio
from rest_framework.permissions import AllowAny 
from django.contrib.auth.models import User
from .models import Perfil # Necesario para PerfilViewSet

# Importamos todos los serializers
from .serializers import RegistroUsuarioSerializer, UsuarioAdminSerializer, PerfilSerializer 
# Importamos todas las clases de permiso que creamos (¡Corregido!)
from .permissions import IsAdministrador, IsRecepcionista, IsOwnerOrAdmin 


# =========================================================
# 1. VISTA DE REGISTRO (US-001) - ABIERTA
# (Usamos CreateAPIView para simplificar la lógica)
# =========================================================
class RegisterUserView(CreateAPIView):
    """
    Endpoint para el registro público de nuevos usuarios (rol CLIENTE por defecto).
    URL: /api/auth/register/
    """
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer
    # Permiso: Cualquiera puede acceder para registrarse
    permission_classes = [AllowAny] 


# =========================================================
# 2. VIEWSET DE GESTIÓN DE USUARIOS (CRUD) - PROTEGIDA POR ROL
# (Implementa permisos dinámicos con get_permissions)
# =========================================================
class UserViewSet(viewsets.ModelViewSet):
    """
    Permite la gestión total de usuarios.
    Permisos: Admin/Recepcionista (listar/crear) y Dueño/Admin (detalles/edición).
    """
    # Optimización: Carga el perfil junto con el usuario para evitar consultas N+1
    queryset = User.objects.all().prefetch_related('perfil').order_by('-date_joined')
    serializer_class = UsuarioAdminSerializer
    
    # Lógica de permisos detallada basada en la acción
    def get_permissions(self):
        # Listar y Crear usuarios nuevos requiere personal de staff (Recepcionista o Admin)
        if self.action in ['list', 'create']:
            self.permission_classes = [IsRecepcionista]
        # Para ver detalles (retrieve), Actualizar o Eliminar, requiere ser el Dueño O un Administrador
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrAdmin] 
        else:
            # Por defecto, cualquier otra acción requiere estar autenticado
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()


# =========================================================
# 3. VIEWSET DE GESTIÓN DE PERFILES (CRUD) - PROTEGIDA POR ROL
# (Permite la edición directa de los datos del perfil)
# =========================================================
class PerfilViewSet(viewsets.ModelViewSet):
    """
    Gestión directa del modelo Perfil. 
    Usado para que los usuarios puedan editar sus propios datos (teléfono, etc.).
    """
    queryset = Perfil.objects.all().select_related('usuario')
    serializer_class = PerfilSerializer

    def get_permissions(self):
        # Listar requiere personal de staff (Recepcionista o Admin)
        if self.action == 'list':
            self.permission_classes = [IsRecepcionista]
        # CRUD de objeto requiere ser Dueño O Admin
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrAdmin] 
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()