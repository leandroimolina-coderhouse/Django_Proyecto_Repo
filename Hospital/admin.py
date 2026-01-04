from django.contrib import admin
from Hospital.models import *


#admin.site.register(DepartamentoMedico)

@admin.register(DepartamentoMedico)
class DepartamentoMedicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nro_departamento", "email_dpto", "fecha_de_creacion")
    list_display_links = ("nombre",)
    search_fields = ("nro_departamento",)
    list_filter = ("fecha_de_creacion",)
    ordering = ("nro_departamento", "nombre")
    readonly_fields = ("fecha_de_creacion",)
