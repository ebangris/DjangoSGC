from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # todo el que llegue al blog entrara a esta vista
    path('login', views.login),

    #path('post/<int:pk>/', views.post_detail, nombre='post_detail'), # url para los detalles
]