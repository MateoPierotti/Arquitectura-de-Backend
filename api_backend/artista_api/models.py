from django.db import models

# Create your models here.



class Artista(models.Model):
    name = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.name
    
class Cancion(models.Model):
    Nombre = models.CharField(max_length=128)
    artista = models.ForeignKey(Artista, related_name='canciones', on_delete=models.CASCADE)
    fechaDeLanzamiento = models.DateField()
    reproducciones = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.Nombre}'