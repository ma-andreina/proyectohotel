from rest_framework import viewsets
from .models import ReservaRestaurante
from .serializers import ReservaRestauranteSerializer

class ReservaRestauranteViewSet(viewsets.ModelViewSet):
    queryset = ReservaRestaurante.objects.all()
    serializer_class = ReservaRestauranteSerializer