from rest_framework import viewsets
from .models import Plato
from .serializers import PlatoSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer