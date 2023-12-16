from django.shortcuts import render

# Create your views here.
import logging
from random import *
from django.http import HttpResponse
from .models import User, Product, Order

from django.core.management.base import BaseCommand

#from .forms import UserForm
from .forms import UserForm, ManyFieldsForm

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        age = form.cleaned_data['age']
    # Делаем что-то с данными
        logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
    # Делаем что-то с данными 
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
        return render(request, 'myapp4/many_fields_form.html', {'form': form})


def index(request):
    logger.info('BASIS page accessed')
    return HttpResponse(f'ВЫ НА ГЛАВНОЙ СТРАНИЦЕ (DJANGO)<br><br>Используя URLconf, определенный в basisapp.urls, Django попробовал эти шаблоны URL в следующем порядке:<br> admin/<br>fake_data/<int:count><br>product_table/<int:count>')
    #user/<br>order/<br>product/<br>user_order/<int:day>' 
    

def fake_data(request, count):   # заполняем тестовую базу
    #x = 1  # if needed password
    for i in range(count*5):
        y = randint(111, 999)
        product = Product(product=f'Товар{y}', 
                          description=f'Описание {y}',  
                          price=randint(1, 10), 
                          quantity=randint(1, 100), 
                          date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
                          is_deleted=f'{0}',
                          )
        product.save()
    logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА ТОВАРОВ')    
    for i in range(count):
        y = randint(111, 999)
        users = User(first_name=f'Имя{y}', 
                    last_name=f'Фамилия{y}', 
                    email=f'mail{y}@mail.ru', 
                    tel=f'+7800{randint(1111111, 9999999)}',
                    adress=f'Адрес {y}', 
                    date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
                    is_deleted=f'{0}',
                    #password=f'{y}',
                    )
        users.save()
        for i in range(count*3):
            y = randint(111, 999)
            #x = randint(1, count*5)
            order=Order(user=users,
                        product = Product.objects.get(id=randint(1, count*5)),
                        date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
                        total_price=product.price*product.quantity,
                        is_deleted=f'{0}',
                        )
            order.save()
        logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА ЗАКАЗОВ')
        #users.save()    
    logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА КЛИЕНТОВ')

    
    # return HttpResponse('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА ЗАКАЗОВ')   
    return HttpResponse(f'ОБНОВЛЕНА БАЗА ЗАКАЗОВ<br>y = {y}<br>user={users}<br>product={product}<br>цена = {product.price}<br>количество = {product.quantity}<br>total_price = {order.total_price}<br>product id = {product.id}<br><br>id ={Product.objects.get(id=randint(1, count*5))}<br>цена = {product.price}<br>количество = {product.quantity}<br>total_price = {order.total_price}<br>product id = {product.id}')  
