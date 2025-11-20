from rest_framework import viewsets
from .models import TarifaDinamica
from .serializers import TarifaDinamicaSerializer

class TarifaDinamicaViewSet(viewsets.ModelViewSet):
    queryset = TarifaDinamica.objects.all()
    serializer_class = TarifaDinamicaSerializer