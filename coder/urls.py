#PAra generar los path al servidor de django (ej \admin)
from django.urls import path
from .views import index


#Crear la variable porque es asi como django detecta las urls (siempre es una lista, porque estan todas las urls de la app que estamos creando)

urlpatterns = [
    #1 la url, despues la view, y despues le damos un nombre
    path("", index, name ="index"), 
]