# reserva_habitacion/views.py

# reserva_habitacion/views.py

from rest_framework import viewsets, permissions
from .models import ReservaHabitacion
from .serializers import ReservaHabitacionSerializer
from usuarios.permissions import IsAdministrador, IsRecepcionista, IsOwnerOrAdmin
# IMPORTANTE: Importamos la tarea
from .tasks import enviar_email_confirmacion

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
        if self.action in ['list', 'create']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        # 1. Guardamos la reserva vinculándola al usuario actual
        instance = serializer.save(usuario=self.request.user)

        # 2. DISPARADOR DE CELERY: Llamamos a la tarea con el ID real
        print(f"DEBUG: Reserva {instance.pk} creada. Enviando a Celery...")
        enviar_email_confirmacion.delay(instance.pk)