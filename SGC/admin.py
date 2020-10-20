from django.contrib import admin
from .models import *

# admin.site.register(Question, QuestionAdmin)

class Procesos_adm(admin.ModelAdmin):
	list_display = ('nombre', 'codigo', 'tipo')

class Procedimiento_adm(admin.ModelAdmin):
	list_display = ('nombre', 'proceso')
	list_filter=['proceso']
	
admin.site.register(Proceso, Procesos_adm)
admin.site.register(Procedimiento, Procedimiento_adm)
admin.site.register(Indicador)
