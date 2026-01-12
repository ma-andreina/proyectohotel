# proyectohotel-backend/backend/usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Perfil # <-- Importamos el modelo Perfil corregido

# =========================================================
# CLASE INLINE PARA MOSTRAR EL PERFIL DENTRO DEL USUARIO
# =========================================================

class PerfilInline(admin.StackedInline):
    """
    Permite editar los campos del modelo Perfil (como el rol)
    directamente en la vista de edición del User.
    """
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil de Usuario (Rol y Datos)'
    # Campos que el administrador puede ver/editar
    fields = ('rol', 'telefono', 'documento_identidad') 
    
# =========================================================
# CLASE CUSTOM PARA REGISTRAR EL USUARIO
# =========================================================

class UsuarioAdmin(UserAdmin):
    """
    Extiende el administrador de User de Django para incluir la información
    del Perfil de forma integrada.
    """
    inlines = (PerfilInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_rol')
    
    def get_rol(self, obj):
        """Muestra el rol en la lista de usuarios."""
        try:
            return obj.perfil.get_rol_display()
        except Perfil.DoesNotExist:
            return "N/A"
    get_rol.short_description = 'Rol'

# =========================================================
# REGISTRO
# =========================================================

# 1. Desregistramos el modelo User por defecto
admin.site.unregister(User)

# 2. Registramos el modelo User con nuestro administrador customizado
admin.site.register(User, UsuarioAdmin)
