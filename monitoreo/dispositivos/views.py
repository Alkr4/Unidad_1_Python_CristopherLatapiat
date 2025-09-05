from django.shortcuts import render,redirect, get_object_or_404
from .models import Dispositivo
from .forms import DispositivoForm

# Create your views here.

def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(request, "dispositivos/inicio.html",{"dispositivos": dispositivos})

def dispositivo (request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)

    return render (request, "dispositivos/dispositivo.html",{"dispositivo":dispositivo})

def crear_dispositivo(request):
    if request.method == "POST":
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispositivos")
    else:
        form = DispositivoForm()

    return render(request, "dispositivos/crear.html",{"form":form})

def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect("dispositivos")
    else:
        form = DispositivoForm(instance=dispositivo)

    return render(request, "dispositivos/editar.html",{"form":form})

def eliminar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == "POST":
        dispositivo.delete()
        return redirect("dispositivos")

    return render(request, "dispositivos/eliminar.html",{"dispositivo":dispositivo})

def panel_dispositivos(request):
    dispositivos = [
        {"nombre":"Sensor Temperatura","consumo":50},
        {"nombre":"Medidor Solar","consumo":120},
        {"nombre":"Sensor Movimiento","consumo":30},
        {"nombre":"Calefactor","consumo":200},
        {"nombre":"Prueba Exceso","consumo":500},
        {"nombre":"Prueba Correcto","consumo":40},
    ]

    consumo_maximo = 100

    return render(request, "dispositivos/panel.html",{
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })

