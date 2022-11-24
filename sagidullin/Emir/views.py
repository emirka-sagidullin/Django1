from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fio(request, **kwargs):
    return HttpResponse(kwargs['fio'])

def about(request):
    return HttpResponse("Приехал из Казани <br> Успеваемость 4,95 <br> Люблю учиться")

def contacts(request):
    return HttpResponse("Телеграм: @zzerrozz <br> Вк: @feechka_emirka <br> GitHub: emirka-sagidullin")