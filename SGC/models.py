from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

class Proceso(models.Model):
	#Tipos = models.TextChoices('Tipos', 'Misionales Operativos Apoyo')
	Tipos = ('misionales', 'Misionales'), ('operativos', 'Operativos'), ('apoyo', 'Apoyo')
	nombre = models.CharField(max_length=80)
	codigo = models.CharField(max_length=15)
	
	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	# Un proceso pertenece a un tipo de procesos
	tipo = models.CharField(choices=Tipos, max_length=10)

	def __str__(self):
		return self.nombre

class Procedimiento(models.Model):
	nombre = models.CharField(max_length=80)
	detalles = models.TextField()

	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	#Un procedimiento pertenece a un proceso
	proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Tarea(models.Model):
	nombre = models.CharField(max_length=80)
	detalles = models.TextField()
	encargado = models.ManyToManyField(User) 
	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	#Una tarea pertenece a un procedimiento
	procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)

	def encargados(self):
		encargados = self.encargado.all()
		return encargados
		
	def __str__(self):
		return self.nombre

class Indicador(models.Model):
	nombre = models.CharField(max_length=80)
	
	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	actual = models.IntegerField()
	esperado = models.IntegerField()

	def calc(self):
		cumplido = (self.actual / self.esperado)*100
		return int(cumplido)

	def __str__(self):
		return self.nombre
	