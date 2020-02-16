from django.db import models


class Despacho(models.Model):
    departamento = models.CharField(max_length = 50, null = False, blank = False, default = 'santander')
    ciudad = models.CharField(max_length = 50, null = False, blank = False, default = 'bucaramanga')
    corporacion = models.CharField(max_length = 50, null = False, blank = False, default = 'juzgado de circuito 31')
    especialidad = models.CharField(max_length = 50, null = False, blank = False, default = 'penal')
    despacho = models.CharField(max_length = 100, null = False, blank = False, default = 'juzgado de circuito penal 01')
    direccion = models.CharField(max_length = 100, null = False, blank = False, default = 'avenida siempre viva 742')
    telefono = models.CharField(max_length = 20, null = False, blank = False, default = '666')