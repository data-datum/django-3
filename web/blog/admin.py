from django.contrib import admin
from .models import *

# Register your models here.


class CursoAdmin(admin.ModelAdmin):

    list_display = ('curso', 'institucion', 'horas', 'anio')
    search_fields = ('curso', 'institucion', 'horas', 'anio')

class WorkshopAdmin(admin.ModelAdmin):

    list_display = ('workshop', 'anio')
    search_fields = ('workshop', 'anio')
    
class PosteoAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'autor')


admin.site.register(cursos_dictados, CursoAdmin)
admin.site.register(workshops, WorkshopAdmin)
admin.site.register(Avatar)
admin.site.register(Posteo, PosteoAdmin)