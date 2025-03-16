from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    edat= models.DateField(max_length=500)
    genere =models.CharField(max_length=500)
    curs  =models.CharField(max_length=500)
    moduls =models.CharField(max_length=500)
    tutor = models.CharField(max_length=500)


class Alumne(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    edat= models.DateField(max_length=500)
    genere =models.CharField(max_length=500)
    curs = models.CharField(max_length=500)
    moduls = models.CharField(max_length=500)
    tutor = models.CharField(max_length=500)


