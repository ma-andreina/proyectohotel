from rest_framework import serializers
from .models import TarifaDinamica

class TarifaDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifaDinamica
        fields = '__all__'