from django.contrib import admin
from .models import *

# admin.site.register(Question, QuestionAdmin)

class Procesos(admin.ModelAdmin):
	list_display = ('nombre', 'codigo', 'tipo')

class Procedimientos(admin.ModelAdmin):
	list_display = ('nombre', 'proceso')
	list_filter=['proceso']

class Tareas(admin.ModelAdmin):
	list_display = ('nombre', 'procedimiento')
	list_filter=['procedimiento']
	
admin.site.register(Proceso, Procesos)
admin.site.register(Procedimiento, Procedimientos)
admin.site.register(Tarea, Tareas)
admin.site.register(Indicador)
