from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Client(models.Model):
    IdClient = models.AutoField(primary_key=True)
    NomClient = models.CharField(max_length=50)
    EmailClient = models.EmailField()


class Reservation(models.Model):
    IdReserv = models.AutoField(primary_key=True)
    DateReserv = models.DateTimeField()
    NbPers = models.PositiveSmallIntegerField()


class Command(models.Model):
    IdCommand = models.AutoField(primary_key=True)
    ModeCommand = models.CharField(max_length=20)


class TypePaiement(models.Model):
    IdTypePaie = models.AutoField(primary_key=True)
    IntitulePaie = models.CharField(max_length=20)


class Facture(models.Model):
    IdFacture = models.AutoField(primary_key=True)
    DateFacture = models.DateField()
    DateModifFact = models.DateField()


class Paiement(models.Model):
    IdPaie = models.AutoField(primary_key=True)
    DatePaie = models.DateField()
    CommandId = models.OneToOneField(Command)
    TypePaie = models.ForeignKey(TypePaiement)
    IdFacture = models.OneToOneField(Facture)
