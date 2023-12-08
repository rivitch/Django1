from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import *
from .models import User, Product#, Order

def user_name(request):
    for i in range(3):
        user = User(first_name=f'Имя {i+1}', last_name=f'Фамилия {i+1}', email=f'{i+1}@mail.ru', tel=f'+7800{randint(0000000, 9999999)}', adress=f'Адрес {i+1}', date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        user.save()
    return HttpResponse('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')

def product_name(request):
    for i in range(3):
        product = Product(product=f'Товар {i+1}', description=f'Описание {i+1}',  price=f'Цена {randint(1, 10)}', quantity=f'Количество {i+1}', date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        product.save()
    return HttpResponse('ОБНОВЛЕНА БАЗА ТОВАРОВ')


