from chileApp.models import Region, Provincia, Comuna
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_id', 'region_nombre', 'region_ordinal')


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('provincia_id', 'provincia_nombre','region_id')


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('comuna_id','comuna_nombre','provincia_id')