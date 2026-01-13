from rest_framework import viewsets, permissions
from .models import ReservaRestaurante
from .serializers import ReservaRestauranteSerializer
from .task import enviar_email_restaurante

class ReservaRestauranteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las reservas del restaurante.
    Incluye la lógica para disparar correos de confirmación mediante Celery.
    """
    queryset = ReservaRestaurante.objects.all().select_related('usuario', 'mesa')
    serializer_class = ReservaRestauranteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # 1. Guardamos la instancia de la reserva asignando el usuario actual
        instance = serializer.save(usuario=self.request.user)
        
        # 2. Imprimimos un log de depuración en la terminal de Django
        print(f"DEBUG: Reserva de mesa {instance.codigo_reserva} creada. Enviando a Celery...")
        
        # 3. Disparamos la tarea asíncrona enviando el ID de la reserva
        enviar_email_restaurante.delay(instance.pk)