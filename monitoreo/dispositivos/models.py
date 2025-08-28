from django.db import models

class Medicion(models.Model):
    valor_consumo = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='mediciones')

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.valor_consumo} - {self.fecha_hora}"


class Alerta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='alertas')

    def __str__(self):
        return self.nombre