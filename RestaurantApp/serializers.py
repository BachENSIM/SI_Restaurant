from rest_framework import serializers
from RestaurantApp.models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('IdRestau', 'NomRestau', 'Adresse', 'EmailRestau', 'NumeroRestau', 'Logo', 'DateModifRestau')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('IdMenu', 'Designation', 'DataModifMenu')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('IdTable', 'Capacity', 'Dispo', 'IdRestau')


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = ('IdPlat', 'NomPlat', 'PrixPlat', 'Description', 'DataModifPlat', 'IdMenu', 'IdRestau')


class CodeQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeQR
        fields = ('IdCode', 'Url', 'IdCodeRestau', 'IdCodeTable')
