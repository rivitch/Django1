from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import *
from .models import Author

def author_name(request):
    # var_Y = randint(1900, 2000)
    # var_M = randint(1, 12)
    # var_D = randint(1, 28)
    for i in range(10 ):
        author = Author(first_name=f'Имя {i}', last_name=f'Фамилия {i}', email=f'{i}@mail.ru', biografy=f'Биография {i}', date_of_birth=f'{randint(1900, 2000)}-{randint(1, 12)}-{randint(1, 28)}')
        author.save()

    # site = choice(['орёл', 'решка'])
    # arg = Coin(site=site)
    # arg.save()
    # return HttpResponse(str(site))
    return HttpResponse('12345')
    pass