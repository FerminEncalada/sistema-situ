from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasajeroFormulario
from .models import Pasajero

# Create your views here.

def home_view(request):
    return render(request, "index.html", {})

# READ - Listar todos los pasajeros
def pasajeros(request):
    pasajeros = Pasajero.objects.all()
    return render(request, "pasajeros.html", {"pasajeros": pasajeros})

# CREATE - Crear nuevo pasajero
def pasajerosCrear(request):
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")
    else:
        formulario = PasajeroFormulario()
    return render(request, "pasajerosCrear.html", {"form": formulario})

# UPDATE - Editar pasajero existente
def pasajerosEdit(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")
    else:
        formulario = PasajeroFormulario(instance=pasajero)
    return render(request, "pasajerosEdit.html", {"form": formulario, "pasajero": pasajero})

# DELETE - Eliminar pasajero
def pasajerosEliminar(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    if request.method == 'POST':
        pasajero.delete()
        return redirect(to="pasajeros")
    return render(request, "pasajerosEliminar.html", {"pasajero": pasajero})