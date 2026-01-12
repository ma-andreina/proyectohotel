from rest_framework import viewsets, permissions
from .models import ReservaHabitacion
from .serializers import ReservaHabitacionSerializer
from usuarios.permissions import IsAdministrador, IsRecepcionista, IsOwnerOrAdmin
from django.contrib.auth.models import User # Importamos User

class ReservaHabitacionViewSet(viewsets.ModelViewSet):
    queryset = ReservaHabitacion.objects.all().select_related('usuario', 'habitacion')
    serializer_class = ReservaHabitacionSerializer

    def get_queryset(self):
        user = self.request.user
        if IsAdministrador().has_permission(self.request, self) or IsRecepcionista().has_permission(self.request, self):
            return self.queryset
        if user.is_authenticated:
            return self.queryset.filter(usuario=user)
        return self.queryset.none()

    def get_permissions(self):
        # CAMBIO: Permitimos 'create' a cualquier persona para la prueba
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        # CAMBIO: Si no hay usuario logueado, intentamos usar el ID que viene en el JSON
        usuario_id = self.request.data.get('usuario')
        if usuario_id:
            try:
                usuario = User.objects.get(id=usuario_id)
                serializer.save(usuario=usuario)
            except User.DoesNotExist:
                serializer.save(usuario=self.request.user)
        else:
            serializer.save(usuario=self.request.user)