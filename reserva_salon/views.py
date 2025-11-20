from rest_framework import viewsets
from .models import ReservaSalon
from .serializers import ReservaSalonSerializer

class ReservaSalonViewSet(viewsets.ModelViewSet):
    queryset = ReservaSalon.objects.all()
    serializer_class = ReservaSalonSerializer