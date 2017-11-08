from django.db import models


# Create your models here.
class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_nombre = models.CharField(max_length=64)
    region_ordinal = models.CharField(max_length=4)


class Provincia(models.Model):
    provincia_id = models.IntegerField(primary_key=True)
    provincia_nombre = models.CharField(max_length=64)
    region_id = models.IntegerField()


class Comuna(models.Model):
    comuna_id = models.IntegerField(primary_key=True)
    comuna_nombre = models.CharField(max_length=64)
    provincia_id = models.IntegerField()