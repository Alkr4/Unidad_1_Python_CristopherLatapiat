from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Zona (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Dispositivo (models.Model):
    nombre = models.CharField(max_length=50)
    consumo_maximo = models.IntegerField()
    estado = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
      
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