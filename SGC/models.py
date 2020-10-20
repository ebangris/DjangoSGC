from django.db import models
from django.utils import timezone

class Proceso(models.Model):
	#Tipos = models.TextChoices('Tipos', 'Misionales Operativos Apoyo')
	Tipos = ('misionales', 'Misionales'), ('operativos', 'Operativos'), ('apoyo', 'Apoyo')
	nombre = models.CharField(max_length=80)
	codigo = models.CharField(max_length=15)
	
	creacion = models.DateField()
	edicion = models.DateField()
	
	# Un proceso pertenece a un tipo de procesos
	tipo = models.CharField(choices=Tipos, max_length=10)

	def __str__(self):
		return self.nombre

class Procedimiento(models.Model):
	nombre = models.CharField(max_length=80)
	detalles = models.TextField()

	#Un procedimiento pertenece a un proceso
	proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Tarea(models.Model):
	nombre = models.CharField(max_length=80)
	detalles = models.TextField()

	#Una tarea pertenece a un procedimiento
	procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Indicador(models.Model):
	nombre = models.CharField(max_length=80)
	actual = models.IntegerField()
	esperado = models.IntegerField()
	
	def __str__(self):
		return self.nombre