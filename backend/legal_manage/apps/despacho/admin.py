from django.contrib import admin

from .models.despacho import Despacho
from .models.juez import Juez

admin.site.register(Despacho)
admin.site.register(Juez)