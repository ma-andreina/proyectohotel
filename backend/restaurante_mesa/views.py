from rest_framework import viewsets
from .models import RestauranteMesa
from .serializers import RestauranteMesaSerializer

class RestauranteMesaViewSet(viewsets.ModelViewSet):
    queryset = RestauranteMesa.objects.all()
    serializer_class = RestauranteMesaSerializer