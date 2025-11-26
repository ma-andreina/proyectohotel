# proyectohotel-backend/usuarios/permissions.py
from rest_framework.permissions import BasePermission
from .models import Perfil # Importamos el modelo Perfil que guarda el rol

class IsAdministrador(BasePermission):
    """
    Permite acceso solo a usuarios con rol 'Administrador'.
    Se usa en ViewSets para proteger APIs de administración.
    """
    def has_permission(self, request, view):
        # 1. El usuario debe estar autenticado
        if not request.user.is_authenticated:
            return False
            
        try:
            # 2. Busca el Perfil asociado al usuario actual
            perfil = Perfil.objects.get(usuario=request.user)
            # 3. Retorna True solo si el rol es 'ADMINISTRADOR'
            return perfil.rol == 'ADMINISTRADOR'
        except Perfil.DoesNotExist:
            return False 

class IsRecepcionista(BasePermission):
    """
    Permite acceso solo a usuarios con rol 'Recepcionista' o 'Administrador'.
    Se usa en ViewSets para proteger APIs de operación diaria.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            perfil = Perfil.objects.get(usuario=request.user)
            # Permite a recepcionista y también al administrador (ya que el admin tiene todos los permisos)
            return perfil.rol in ['RECEPCIONISTA', 'ADMINISTRADOR'] 
        except Perfil.DoesNotExist:
            return False
            
