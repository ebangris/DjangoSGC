from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

class Proceso(models.Model):
	#Tipos = models.TextChoices('Tipos', 'Misionales Operativos Apoyo')
	Tipos = ('misionales', 'Misionales'), ('estrategicos', 'Estrategicos'), ('apoyo', 'Apoyo')
	nombre = models.CharField(max_length=80)
	
	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	# Un proceso pertenece a un tipo de procesos
	tipo = models.CharField(choices=Tipos, max_length=12)

	def __str__(self):
		return self.nombre

class Procedimiento(models.Model):
	nombre = models.CharField(max_length=80)
	codigo = models.CharField(max_length=15)
	objetivo = models.TextField()
	alcance = models.TextField()

	# el encargado sera un usuario del sistema
	encargado = models.ManyToManyField(User) 
	
	# el infograma debe ser una imagen, la base de datos almacena el nombre del archivo
	infograma = models.ImageField(blank=True, upload_to='infogramas/')

	def foldername(self, filename):
		return 'formatos/{0}'.format(filename)
	
	# el formato sera un archivo de word o pdf
	formatos = models.FileField(blank=True, upload_to= foldername)

	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	#Un procedimiento pertenece a un proceso
	proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
	
	def encargados(self):
		encargados = self.encargado.all()
		return encargados

	def __str__(self):
		return self.nombre

class Indicador(models.Model):
	nombre = models.CharField(max_length=80)
	
	creacion = models.DateField(auto_now_add=True)
	edicion = models.DateField(auto_now=True)
	
	proposito = models.TextField()
	detalle = models.TextField()
	interpretacion = models.TextField()

	actual = models.IntegerField()
	esperado = models.IntegerField()
	
	fecha_objetivo = models.DateField(default=timezone.now, blank=True)
	
	#Un indicador pertenece a un procedimiento
	procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)

	def calc(self):
		if(self.esperado > 0 ):
			cumplido = (self.actual / self.esperado)*100
		else:
			cumplido = '--'
		return cumplido

	def encargados(self):
		encargados = self.encargado.all()
		return encargados

	def __str__(self):
		return self.nombre
	