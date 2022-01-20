from django.urls import path
# from CursoPython.ProyectoCoder.AppCoder.views import cursos
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
]
