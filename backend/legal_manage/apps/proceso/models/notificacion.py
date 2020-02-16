from django.db import models
from pandas.tseries.offsets import BDay
import pandas
from ...abogado.models.persona import Persona
from .proceso import Proceso

class Notificacion(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length = 60, null = False, blank = False)
    mensaje = models.CharField(max_length = 100, null = False, blank = False)
    expedicion = models.DateTimeField( null = False )
    limite = models.DateField( null = False )

    def fecha_limite(self, fecha, dias):
        """ Esta funcion calcular la fecha limite solo teniendo en cuenta los dias laborales para hacer efectiva la notificacion  """
        fecha_expedicion = datetime.strptime(fecha, '%m-%d-%Y').date()
        limite = fecha_expedicion + BDay(dias)
        self.limite = limite
        return limite



class Notificados(models.Model):
    MEDIOS = ( ('EMAIL', 'email'), ('PERSONAL', 'personal'), ('TELEFONO', 'telefono') )  
    persona = models.ForeignKey( Persona, on_delete=models.CASCADE )
    notificacion = models.ForeignKey( Notificacion, on_delete=models.CASCADE )
    notificado = models.BooleanField( default = False )
    medio = models.CharField( max_length = 30, null = False, choices = MEDIOS, default = 'EMAIL', blank = False )

