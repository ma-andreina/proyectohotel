# proyectohotel-backend/usuarios/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny # Necesario para el registro público
from django.contrib.auth.models import User # <-- Usamos el modelo User de Django

# Importamos los serializers que creamos
from .serializers import RegistroUsuarioSerializer, UsuarioAdminSerializer 
# Importamos las clases de permiso para implementar US-003
from .permissions import IsAdministrador 


# =========================================================
# 1. VISTA DE REGISTRO (US-001) - ABIERTA
# =========================================================
class RegistroUsuarioAPIView(APIView):
    """
    API para registrar nuevos usuarios (clientes).
    URL: /api/usuarios/registro/
    """
    # Sobrescribe la configuración global: este endpoint permite el acceso sin autenticación
    permission_classes = [AllowAny] 
    
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Usuario registrado exitosamente. Ahora puede iniciar sesión."}, 
                status=status.HTTP_201_CREATED
            )
        # Retorna los errores de validación si fallan (ej: email duplicado)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================================================
# 2. VIEWSET DE GESTIÓN (CRUD) - PROTEGIDA POR ROL (US-003)
# =========================================================
class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el CRUD de usuarios por parte del personal administrativo (Router).
    """
    # Usamos el modelo User de Django (que es el que tiene la seguridad)
    queryset = User.objects.all() 
    # Usamos el serializer específico para la administración
    serializer_class = UsuarioAdminSerializer 
    
    # ----------------------------------------------------
    # IMPLEMENTACIÓN DEL PERMISO (US-003)
    # Solo permitirá el acceso si el rol del usuario es 'Administrador'.
    # ----------------------------------------------------
    permission_classes = [IsAdministrador]