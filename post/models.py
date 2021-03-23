from django.db import models
from django.urls import reverse
# Create your models here.

class PostAutor(models.Model):
    nombreAutor = models.CharField(max_length=255, default='')
    saga = models.CharField(max_length=255, default='')
    descripcion = models.TextField(default='', blank=True, null=True)
    imagenAutor = models.ImageField(upload_to='static/img/autores')
    def __str__(self):
        return self.saga
    def get_absolute_url(self):
        return reverse('autorDetalle', args=[str(self.pk)])

class PostLibro(models.Model):
    saga = models.ForeignKey(PostAutor, on_delete=models.CASCADE)
    nombreLibro = models.CharField(max_length=255, default='')
    imagenLibro = models.ImageField(upload_to='static/img/libros')
    def __str__(self):
        return self.nombreLibro
    
    def get_absolute_url(self):
        return reverse('autorDetalle', args=[str(self.pk)])