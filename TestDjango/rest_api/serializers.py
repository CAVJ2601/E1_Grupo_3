from rest_framework import serializers
from core.models import Region, Comuna

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id_region','nombre_region']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_comuna','nombre_comuna', 'id_region']