from rest_framework import viewsets, permissions
from .models import ReservaSalon
from .serializers import ReservaSalonSerializer
from .task import enviar_email_salon  # Corregido: .tasks en plural para coincidir con el nombre del archivo

class ReservaSalonViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las reservas del salón de eventos.
    Dispara la tarea asíncrona de email al confirmar la creación.
    """
    queryset = ReservaSalon.objects.all().select_related('usuario', 'salon')
    serializer_class = ReservaSalonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Guardamos la reserva asociándola al usuario que realiza la petición
        instance = serializer.save(usuario=self.request.user)
        
        # Log de depuración en la consola del servidor Django
        print(f"DEBUG: Reserva de salón {instance.codigo_evento} creada con éxito. Enviando a Celery...")
        
        # Disparamos la tarea asíncrona pasando el ID (Primary Key) de la reserva
        enviar_email_salon.delay(instance.pk)