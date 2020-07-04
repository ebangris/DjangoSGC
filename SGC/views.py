from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as do_logout
from django.utils import timezone
from .models import *

# Create your views here.
'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
'''

def login(request):
    return render(request, "index.html")

def index(request):
	# si tiene una sesion iniciada
	if request.user.is_authenticated:
		procesos = Proceso.objects.all() # muestra todos los sistemas de procesos
		return render(request, "index.html", {'Procesos':procesos} )
	
	# si no ha iniciado sesion
	return render(request, "index.html")

