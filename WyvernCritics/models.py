from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):
    tipo = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.tipo


class Person(models.Model):
    name = models.CharField(max_length=50)
    role = models.ManyToManyField(Role)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'person'

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    plot = models.CharField(max_length=500)
    release = models.DateField()
    calificacion = models.DecimalField(max_digits=2, decimal_places=1,
                                       validators=[MaxValueValidator(5), MinValueValidator(0)])
    person = models.ManyToManyField(Person)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.name


class Review(models.Model):
    titulo = models.CharField(max_length=50)
    critica = models.CharField(max_length=500)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1,
                                       validators=[MaxValueValidator(10), MinValueValidator(0)])
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.titulo
