from django.contrib import admin
from .models import *

# admin.site.register(Question, QuestionAdmin)

class Procesos(admin.ModelAdmin):
	list_display = ('nombre', 'tipo')

class Procedimientos(admin.ModelAdmin):
	list_display = ('nombre', 'proceso', 'codigo' )
	list_filter=['proceso']
	
admin.site.register(Proceso, Procesos)
admin.site.register(Procedimiento, Procedimientos)
admin.site.register(Indicador)
