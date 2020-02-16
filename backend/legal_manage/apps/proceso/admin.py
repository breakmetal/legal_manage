from django.contrib import admin
from .models import Actuacion
from .models import Archivos
from .models import Cautelar
from .models import Ejecutivo
from .models import Notificacion
from .models import Proceso

admin.site.register(Actuacion)
admin.site.register(Archivos)
admin.site.register(Cautelar)
admin.site.register(Ejecutivo)
admin.site.register(Notificacion)
admin.site.register(Proceso)
