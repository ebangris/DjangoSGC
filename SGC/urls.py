from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # todo el que llegue al blog entrara a esta vista
	path('proceso/<int:pk>/', views.proceso, name='proceso'),
    path('procedimiento/<int:pk>/', views.procedimiento, name='procedimiento'),
    path('indicadores', views.indicadores, name='indicadores'),
    path('indicadores/<int:pk>/', views.indicador, name='indicador'),

    #path('post/<int:pk>/', views.post_detail, nombre='post_detail'), # url para los detalles
]