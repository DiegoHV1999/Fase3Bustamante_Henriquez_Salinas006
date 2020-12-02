from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class local(models.Model):
    
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    confirmarClave = models.CharField(max_length=200)

    tipo = (
        ('1', 'Gastronomica'),
        ('2', 'Salud'),
        ('3', 'Logistica'),

    )


    tipoEmpresa= models.CharField(
        max_length=1,
        choices= tipo,
        blank = True,
        default = 0,
        help_text= 'Tipo de empresa',
    )

    class meta:
        ordering = ['nombre', 'direccion']
    
    def get_absolute_url(self):
        return reverse('local_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.nombre}, {self.direccion}'

class transporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 9)
    correo = models.EmailField(null=True, blank=True)
    local = models.ForeignKey('local', on_delete=models.SET_NULL,null=True, blank=False)

    class meta:
        ordering = ['nombre', 'correo']

    def get_absolute_url(self):
        return reverse('transporte_detail', args=[str(self.id)])
    
    def __str__(self):
        #return f'{self.nombre}, {self.correo}'
        return self.nombre
    
    


