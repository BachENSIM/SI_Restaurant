from django.db import models


# Create your models here.
class Restaurant(models.Model):
    IdRestau = models.AutoField(primary_key=True)
    NomRestau = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=200)
    EmailRestau = models.EmailField()
    NumeroRestau = models.CharField(max_length=12)
    Logo = models.ImageField(upload_to="images/restaurant")
    DateModifRestau = models.DateField()


class Table(models.Model):
    IdTable = models.AutoField(primary_key=True)
    Capacity = models.IntegerField()
    Dispo = models.BooleanField()
    IdRestau = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class CodeQR(models.Model):
    IdCode = models.AutoField(primary_key=True)
    Url = models.CharField(max_length=200)
    IdRestau = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    IdTable = models.OneToOneField(Table, on_delete=models.CASCADE)


class Menu(models.Model):
    IdMenu = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=50)
    DateModifMenu = models.DateField()
    IdRestau = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Plat(models.Model):
    Idplat = models.AutoField(primary_key=True)
    NomPlat = models.CharField(max_length=50)
    PrixPlat = models.FloatField()
    Description = models.TextField()
    DateModifPlat = models.DateField()
    IdMenu = models.ForeignKey(Menu, on_delete=models.CASCADE)
