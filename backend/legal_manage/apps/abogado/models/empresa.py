from django.db import models
from .abogado import Abogado
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Empresa(models.Model):
    abogado = models.ForeignKey( User, on_delete = models.CASCADE )
    documento = models.FloatField()
    nombre = models.CharField( max_length = 50, null = False, blank = False )
    actividad = models.CharField( max_length = 50, null = False, blank = False )
    
    def contact_default():
       return {'email': 'to1@example.com',
              'direcciones':[{'ubicacion': 'avenida siempre viva 742', 'telefono': '000000', 'descripcion': 'fijo'}]    
       }
    
    contact_info = JSONField( "ContactInfo", default=contact_default )

