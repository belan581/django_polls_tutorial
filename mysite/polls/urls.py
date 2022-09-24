from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hola2/', views.hola_dos, name='hola2'),
]