from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as do_logout
from django.utils import timezone
from SGC.models import *

# Create your views here.
'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
'''

def indicadores(request):
	indicadores = Indicador.objects.all()
	return render(request, "indicadores.html", {'indicadores':indicadores})

def proceso(request, pk):
	proceso = get_object_or_404(Proceso, pk=pk)
	procedimientos = Procedimiento.objects.filter(proceso=proceso)
	return render(request, 'proceso.html', {'proceso':proceso, 'procedimientos':procedimientos})

def procedimiento(request, pk):
	procedimiento = get_object_or_404(Procedimiento, pk=pk)
	tareas = Tarea.objects.filter(procedimiento=procedimiento)
	return render(request, 'procedimiento.html', {'procedimiento':procedimiento, 'tareas':tareas})

def tarea(request, pk):
	tarea = get_object_or_404(Tarea, pk=pk)
	return render(request, 'tarea.html', {'tarea':tarea})

def index(request):
	# si tiene una sesion iniciada
	#if request.user.is_authenticated:
		M = Proceso.objects.filter(tipo='misionales')
		O = Proceso.objects.filter(tipo='operativos')
		A = Proceso.objects.filter(tipo='apoyo')
		return render(request, "index.html", {'Misionales':M, 'Operativos':O, 'Apoyo':A} )
	
	# si no ha iniciado sesion
	#return render(request, "Error404")

