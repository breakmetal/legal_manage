from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Abogado(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    documento = models.FloatField(primary_key=True)
    telefono = models.CharField(max_length = 50, null = False, blank = False, default = '555')
    especialidad = models.CharField(max_length = 50, null = False, blank = False, default = '555')
    nacimiento = models.DateField(default=datetime.now)





