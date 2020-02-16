from .despacho import Despacho
from django.db import models

class Juez(models.Model):
    documento = models.FloatField(primary_key=True)
    despacho = models.OneToOneField(Despacho, on_delete = models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length = 100, null = False, blank = False)