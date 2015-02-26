from django.contrib import admin
from horarios.apps.fichas.models import *

#admin.site.register(Tipo_Persona)
#admin.site.register(Persona)
#admin.site.register(Dia)

class Horario_admin(admin.ModelAdmin):
	list_display = ('fecha',)

admin.site.register(Instructor)

admin.site.register(Programa)
admin.site.register(Tipo_Programa)
admin.site.register(Jornada)




admin.site.register(Aprendiz)
admin.site.register(Ficha)
admin.site.register(Franja)
admin.site.register(Evento)
admin.site.register(Horario, Horario_admin)