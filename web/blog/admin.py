from django.contrib import admin

# Register your models here.

from .models import *

class CursoAdmin(admin.ModelAdmin):

    list_display = ('curso', 'anio')
    search_fields = ('curso', 'anio')

class WorkshopAdmin(admin.ModelAdmin):

    list_display = ('workshop', 'anio')
    search_fields = ('workshop', 'anio')


admin.site.register(cursos_dictados, CursoAdmin)
admin.site.register(workshops, WorkshopAdmin)
admin.site.register(Avatar)