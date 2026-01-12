# proyectohotel-backend/usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import Perfil, ROLES_USUARIO # Asegúrate de importar ROLES_USUARIO

# =========================================================
# 1. SERIALIZER PARA REGISTRO (US-001) - ABIERTO AL PÚBLICO
# (TU CÓDIGO ACTUAL - CORRECTO)
# =========================================================

class RegistroUsuarioSerializer(serializers.Serializer):
    # ... [Tu código de RegistroUsuarioSerializer es correcto, lo mantendremos] ...
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True) 
    telefono = serializers.CharField(required=False, allow_blank=True)
    documento_identidad = serializers.CharField(required=True)
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

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
# 2. SERIALIZER STANDALONE PARA PERFIL (Para gestión CRUD de perfiles)
# =========================================================

class PerfilSerializer(serializers.ModelSerializer):
    # Campo de lectura para mostrar el nombre completo del usuario
    nombre_completo = serializers.CharField(source='usuario.get_full_name', read_only=True)
    # Campo de lectura para mostrar el username
    username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Perfil
        fields = ['id', 'username', 'nombre_completo', 'rol', 'telefono', 'documento_identidad']
        read_only_fields = ['id', 'username', 'documento_identidad'] # No se permite cambiar el documento ni el id

# =========================================================
# 3. SERIALIZER PARA GESTIÓN ADMIN (UsuarioViewSet) - CORREGIDO
# =========================================================

class UsuarioAdminSerializer(serializers.ModelSerializer):
    # Hacemos que los campos del Perfil sean de escritura y lectura, para que puedan ser editados
    rol = serializers.ChoiceField(choices=ROLES_USUARIO, source='perfil.rol')
    telefono = serializers.CharField(source='perfil.telefono', required=False, allow_blank=True)
    documento_identidad = serializers.CharField(source='perfil.documento_identidad', read_only=True) # Solo lectura para el documento
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'is_active', 'is_staff', 
            'rol', 'telefono', 'documento_identidad'
        ]
        # Permitimos cambiar el email y nombre, pero no el username (identificador)
        read_only_fields = ['username', 'id', 'documento_identidad'] 

    # Implementación del método UPDATE para manejar User y Perfil en una sola solicitud
    @transaction.atomic
    def update(self, instance, validated_data):
        # 1. Extraer los datos que pertenecen al Perfil (usando 'pop' para removerlos)
        perfil_data = validated_data.pop('perfil', {})
        
        # 2. Actualizar los campos del modelo User
        instance = super().update(instance, validated_data)
        
        # 3. Actualizar los campos del modelo Perfil relacionado
        perfil = instance.perfil
        if 'rol' in perfil_data:
            perfil.rol = perfil_data['rol']
        if 'telefono' in perfil_data:
            perfil.telefono = perfil_data['telefono']
            
        perfil.save()
        
        return instance