from django import forms
from django.forms import DateField
 
class CursoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    curso = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class EntregableFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    fechaentrega= forms.DateField()
    entregado= forms.BooleanField()