import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RestaurantApp.serializers import *
from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def restaurant_api(request, id=0):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(restaurant_serializer.data, safe=False)
    elif request.method == "POST":
        restaurant_data = JSONParser().parse(request)
        restaurant_serializer = RestaurantSerializer(data=restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add")
    elif request.method == "PUT":
        restaurant_data = JSONParser().parse(request)
        restaurant = Restaurant.objects.get(IdRestau=restaurant_data['IdRestau'])
        restaurant_serializer = RestaurantSerializer(restaurant, data=restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        restaurant = Restaurant.objects.get(IdRestau=id)
        restaurant.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def code_qr_api(request, id=0):
    if request.method == "GET":
        codes = CodeQR.objects.all()
        code_serializer = CodeQRSerializer(codes, many=True)
        return JsonResponse(code_serializer.data, safe=False)
    elif request.method == "POST":
        code_data = JSONParser().parse(request)
        code_serializer = CodeQRSerializer(data=code_data)
        if code_serializer.is_valid():
            code_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add")
    elif request.method == "PUT":
        code_data = JSONParser().parse(request)
        code = CodeQR.objects.get(IdCode=code_data['IdCode'])
        code_serializer = CodeQRSerializer(code, data=code_data)
        if code_serializer.is_valid():
            code_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        code = CodeQR.objects.get(IdCode=id)
        code.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def menu_api(request, id=0):
    if request.method == "GET":
        menus = Menu.objects.all()
        menu_serializer = Menu(menus, many=True)
        return JsonResponse(menu_serializer.data, safe=False)
    elif request.method == "POST":
        menu_data = JSONParser().parse(request)
        menu_serializer = MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add")
    elif request.method == "PUT":
        menu_data = JSONParser().parse(request)
        menu = Menu.objects.get(IdMenu=menu_data['IdMenu'])
        menu_serializer = MenuSerializer(menu, data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        menu = Menu.objects.get(IdMenu=id)
        menu.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def plat_api(request, id=0):
    if request.method == "GET":
        plats = Plat.objects.all()
        plat_serializer = Plat(plats, many=True)
        return JsonResponse(plat_serializer.data, safe=False)
    elif request.method == "POST":
        plat_data = JSONParser().parse(request)
        plat_serializer = PlatSerializer(data=plat_data)
        if plat_serializer.is_valid():
            plat_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add")
    elif request.method == "PUT":
        plat_data = JSONParser().parse(request)
        plat = Plat.objects.get(IdPlat=plat_data['IdPlat'])
        plat_serializer = PlatSerializer(plat, data=plat_data)
        if plat_serializer.is_valid():
            plat_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        plat = Plat.objects.get(IdPlat=id)
        plat.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def table_api(request, id=0):
    if request.method == "GET":
        tables = Table.objects.all()
        table_serializer = Table(tables, many=True)
        return JsonResponse(table_serializer.data, safe=False)
    elif request.method == "POST":
        table_data = JSONParser().parse(request)
        table_serializer = TableSerializer(data=table_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add")
    elif request.method == "PUT":
        table_data = JSONParser().parse(request)
        table = Table.objects.get(IdTable=table_data['IdTable'])
        table_serializer = TableSerializer(table, data=table_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        table = Table.objects.get(IdTable=id)
        table.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def file_transfer_api(request):
    file = request.FILES['file']
    extension = file.name.split(".")[-1]
    file_extensions = {
        "image": ['png', 'jpg', 'jpeg', 'svg', 'gif'],
        "file": ["pdf", "csv"]
    }
    if extension in file_extensions['image']:
        default_storage.save(os.path.join("images/", file.name), file)
    if extension in file_extensions['file']:
        default_storage.save(os.path.join("files/", file.name), file)
    return JsonResponse(file.name, safe=False)
