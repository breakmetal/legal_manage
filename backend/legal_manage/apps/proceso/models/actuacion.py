from django.db import models
from .proceso import Proceso

class Actuacion(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=True, null=True)
    actuacion = models.CharField(max_length = 60, null = False, blank = False)
    Anotacion = models.CharField(max_length = 100, null = False, blank = False)
    inicio = models.DateTimeField( null = False )
    termino = models.DateTimeField( null = False )
    registro = models.DateTimeField( null = False )
