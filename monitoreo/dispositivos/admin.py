from django.contrib import admin
from .models import Dispositivo, Categoria, Zona, Alerta, Medicion 

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'consumo_maximo', 'categoria', 'estado', 'zona')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class AlertaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_hora', 'dispositivo')

class MedicionAdmin(admin.ModelAdmin):
    list_display = ('valor_consumo', 'fecha_hora', 'dispositivo')

admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Alerta, AlertaAdmin)
admin.site.register(Medicion, MedicionAdmin)