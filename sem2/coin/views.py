from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from .models import choice
from random import *
from .models import Coin

def game_coin(request):
    site = choice(['орёл', 'решка'])
    arg = Coin(site=site)
    arg.save()
    return HttpResponse(str(site))

def coin_values(request):
    value=Coin.values()
    print(value)
    lst=[]
    for i in value:
        print(i)
        lst.append(i)
    return HttpResponse(lst)

