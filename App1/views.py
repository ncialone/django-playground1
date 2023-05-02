from django.shortcuts import render
from django.forms import DateField
from django.http import HttpResponse
from App1.models import Curso, Profesor, Estudiante, Entregable
from App1.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def cursos(request):
    return render(request,'App1/cursos.html')
def profesores(request):
    return render(request,'App1/profesores.html')
def estudiantes(request):
    return render(request,'App1/estudiantes.html')
def entregables(request):
    return render(request,'App1/entregables.html')

def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Profesor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = ProfesorFormulario()       
    return render(request, "App1/profesorFormulario.html", {"miFormulario": miFormulario})

def estudianteFormulario(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Estudiante(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                informacion['email'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = ProfesorFormulario()       
    return render(request, "App1/estudianteFormulario.html", {"miFormulario": miFormulario})

def entregableFormulario(request):
    if request.method =="POST":
        miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
                                                                                #LA FECHA SE INGRESA EN FORMATO YYYY-MM-DD!!!!!!!
            curso = Entregable(int(informacion['id']),str(informacion['nombre']),(informacion['fechaentrega']), 
                                bool(['entregado'])) 
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = EntregableFormulario()       
    return render(request, "App1/entregableFormulario.html", {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request,'App1/busquedaCurso.html')

def buscar(request):
    if request.GET['curso']:
        curso = request.GET['curso']
        cursos= Curso.objects.filter(curso__exact=curso) #LLEGA EL CURSO, FILTRAMOS Y BUSCAMOS EN BD
        if cursos.exists():
            return render(request,'App1/resultadosBusqueda.html', {"cursos":cursos, "comisiones": curso })
        else:
            respuesta= "Datos no encontrados"      
    return HttpResponse(respuesta)
