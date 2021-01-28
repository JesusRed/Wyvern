from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Create your models here.

class Poster(models.Model):
    titulo = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='posters')
    calificacion = models.DecimalField(max_digits=2, decimal_places=1,
                                       validators=[MaxValueValidator(5), MinValueValidator(0)])
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'poster'
        verbose_name_plural = 'posters'

    def __str__(self):
        return self.titulo
