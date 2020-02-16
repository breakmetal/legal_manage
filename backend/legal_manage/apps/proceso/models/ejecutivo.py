from django.db import models
from .proceso import Proceso
from django.contrib.postgres.fields import JSONField

class Ejecutivo(models.Model):
    OBLIGACION = (('DAR', 'dar'), ('HACER', 'hacer'), ('NO_HACER', 'no hacer'))
    TITULO = (('VALOR', 'valor'), ('EJECUTIVO', 'ejecutivo'))
    proceso = models.OneToOneField( Proceso, on_delete = models.CASCADE )
    def pretencion_default():
       return {
              'pretencion':[{'nombre': 'pepito', 'pretencion': '000000', 'descripcion': 'mucho dinero'}]    
       }
    
    contact_info = JSONField( "ContactInfo", default=pretencion_default )
    titulo = models.CharField( max_length = 9, null = False, choices = TITULO, default = 'VALOR')
    obligacion = models.CharField( max_length = 8, null = False, choices = OBLIGACION, default = 'DAR')
    cuantia = models.CharField(max_length = 6,  null = False, default = 'minima' )


    def calcular_cuantia(self):
        valor = self.pretencion/87780300 
        if valor<=40:
            self.cuantia = 'minima'
        if valor>40 and valor<=150:
            self.cuantia = 'menor'
        else:
            self.cuantia = 'mayor'
    