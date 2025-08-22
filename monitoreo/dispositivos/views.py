from django.shortcuts import render


# Create your views here.
"""
def inicio(request):
    contexto = {"nombre":"Cris"}
    return render(request, "dispositivos/inicio.html",contexto)
"""

def panel_dispositivos(request):
    dispositivos = [
        {"nombre":"Sensor Temperatura","consumo":50},
        {"nombre":"Medidor Solar","consumo":120},
        {"nombre":"Sensor Movimiento","consumo":30},
        {"nombre":"Calefactor","consumo":200},
    ]

    consumo_maximo = 100

    for cosa in dispositivos:
        print([0])

    return render(request, "dispositivos/panel.html",{
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })

