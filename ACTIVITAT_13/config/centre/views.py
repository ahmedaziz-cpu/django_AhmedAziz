from re import template

from Tools.scripts.generate_opcode_h import header
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import request
from .forms import professorForm
from .forms import alumneForm
from .models import Alumne, Professor


#from config.centre.models import Alumne


# Create your views here.
def index(request):

    return render(request,'index.html',{'index':index})




def professors(request):
    #professors = [
     #   {"name": "Davids", "surname": "Ismael", "email": "davids@gmail.com", "age": "20", "genero": "Masculino"},
      #  {"name": "Daniel", "surname": "Cubias", "email": "daniel@gmail.com", "v.age": "25", "genero": "NULL"},
       # {"name": "Ahmed", "surname": "Aziz", "email": "Ah39aziz@gmail.com", "age": "20", "genero": "Masculino"}
    #]

    # Pasamos la lista 'professors' al template
    professors = Professor.objects.all()
    return render(request, 'professors.html', {'professors': professors})


def alumnes(request):
    #alumnes =  [
     #   {"name": "Davids", "surname": "Ismael", "email": "davids@gmail.com", "age": "20", "genero": "Masculino"},
      #  {"name": "Daniel", "surname": "Cubias", "email": "daniel@gmail.com", "v.age": "25", "genero": "NULL"},
       # {"name": "Ahmed", "surname": "Aziz", "email": "Ah39aziz@gmail.com", "age": "20", "genero": "Masculino"}
    #]
    alumnes = Alumne.objects.all()
    return render(request,'alumnes.html',{'alumnes':alumnes})


def alumnes_detalles(request, pk):
    try:
        alumne = Alumne.objects.get(pk=pk)
    except Alumne.noexiste:
        alumne = None
    return render(request, 'alumnes_detalles.html', {'alumne': alumne})

def professors_detalles(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.noexiste:
        professor = None
    return render(request, 'professors_detalles.html', {'professor': professor})

def books(request):
    books =  [
         {"id":"2","autor":"yo","titol":""},
         {"id":"2","autor":"","titol":"yo"},
         {"id":"2","autor":"yo","titol":"yo"}
]
    return render(request,'books.html',{'books':books})

def book(request, bk):
 book_Obj = None
 for i in books:
        if i['id'] == bk:
            book_Obj = i
 return render(request,'books.html',{'books':book_Obj})

def user_form(request):
    form = alumneForm()

    if request.method == 'POST':
        form = alumneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'alumne_form': form}
    return render(request, 'alumne_form.html', context)

def users_form(request):
    form = professorForm()

    if request.method == 'POST':
        form = professorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'professor_form': form}
    return render(request, 'professor_form.html', context)




