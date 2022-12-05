from django.contrib import admin
from .models import Region, Provincia, Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_filter = ['provincia']


admin.site.register(Region)
admin.site.register(Provincia)
