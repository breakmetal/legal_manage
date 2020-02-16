from django.db import models
from .proceso import Proceso

class Archivos(models.Model):
    TIPOS = (
        ('IMAGENES', 'imagenes'),
        ('PDF', 'pdf'),
        ('WORD', 'word'),
    )
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length = 15, null = False, choices = TIPOS, default = TIPOS, blank = False)
    documento =  models.CharField(max_length = 30, null = False,  blank = False)
    extencion = models.CharField(max_length = 10, null = False,  blank = False)
    ruta = models.CharField(max_length = 50, null = False,  blank = False)
    descripcion = models.CharField(max_length = 100, null = False,  blank = False)