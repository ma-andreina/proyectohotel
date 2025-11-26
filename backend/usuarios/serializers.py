# proyectohotel-backend/usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import Perfil 

# =========================================================
# 1. SERIALIZER PARA REGISTRO (US-001) - ABIERTO AL PÚBLICO
# =========================================================

class RegistroUsuarioSerializer(serializers.Serializer):
    """
    Serializer para manejar la validación y creación de un nuevo User y su Perfil.
    """
    # Campos del modelo User (requeridos para el login)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    # La contraseña solo se usa para escribir (POST), nunca para leer (GET)
    password = serializers.CharField(write_only=True) 
    
    # Campos del modelo Perfil (datos adicionales)
    telefono = serializers.CharField(required=False, allow_blank=True)
    documento_identidad = serializers.CharField(required=True)
    
    # Validación: Asegura que el email sea único
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

    # Creación segura del User de Django y el Perfil en una transacción
    @transaction.atomic
    def create(self, validated_data):
        # 1. Crea el objeto User (con la contraseña hasheada)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=False 
        )
        
        # 2. Crea el objeto Perfil asociado al nuevo usuario
        Perfil.objects.create(
            usuario=user,
            telefono=validated_data.get('telefono', ''),
            documento_identidad=validated_data['documento_identidad'],
            rol='CLIENTE' # Rol por defecto para el registro público
        )
        return user

# =========================================================
# 2. SERIALIZER PARA GESTIÓN ADMIN (UsuarioViewSet) - PROTEGIDO (US-003)
# =========================================================
# Este serializer se usa en el UsuarioViewSet del Router para ver y editar usuarios por parte del Admin.

class UsuarioAdminSerializer(serializers.ModelSerializer):
    # Usamos source='perfil.<campo>' para obtener datos del modelo Perfil relacionado
    rol = serializers.CharField(source='perfil.rol', read_only=True)
    telefono = serializers.CharField(source='perfil.telefono', read_only=True)
    documento_identidad = serializers.CharField(source='perfil.documento_identidad', read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'is_active', 'is_staff', 
            'rol', 'telefono', 'documento_identidad' # Incluye campos del Perfil
        ]
        read_only_fields = ['username', 'email'] # Campos clave que el Admin no debería cambiar fácilmente