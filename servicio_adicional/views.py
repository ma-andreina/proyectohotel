from rest_framework import viewsets
from .models import ServicioAdicional
from .serializers import ServicioAdicionalSerializer

class ServicioAdicionalViewSet(viewsets.ModelViewSet):
    queryset = ServicioAdicional.objects.all()
    serializer_class = ServicioAdicionalSerializer