from django.shortcuts import render

# Create your views here.

def index(request): #request siempre va, es la peticion 
    return render(request, "coder/index.html") #coder la app /el archivo (solo eso ya lo reconocera)
    