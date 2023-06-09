from django.contrib import admin
from .models import Categoria, Trabajador, Comunicado

admin.site.register(Categoria)
admin.site.register(Trabajador)

class ComunicadoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Comunicado, ComunicadoAdmin)
