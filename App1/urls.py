from django.urls import path
from App1 import views

urlpatterns = [

    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('estudianteFormulario', views.estudianteFormulario, name="EstudianteFormulario"),
    path('entregableFormulario', views.entregableFormulario, name="EntregableFormulario"),
    path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
    path('buscar/',views.buscar),
]