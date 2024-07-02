from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Equip)
admin.site.register(Ciclista)
admin.site.register(Etapa)