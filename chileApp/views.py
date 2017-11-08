from chileApp.serializers import RegionSerializer, ProvinciaSerializer, ComunaSerializer
from chileApp.models import Region, Provincia, Comuna
from rest_framework import generics


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProvinciaList(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ProvinciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ComunaList(generics.ListCreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class ComunaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
