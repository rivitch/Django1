import logging
              
from random import * # import random
from django.shortcuts import render
#from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from .models import User, Product, Order
#from django.views import View

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

def index(request):
    logger.info('BASIS page accessed')
    return HttpResponse(f'ВЫ НА ГЛАВНОЙ СТРАНИЦЕ (DJANGO)<br><br>Используя URLconf, определенный в basisapp.urls, Django попробовал эти шаблоны URL в следующем порядке:<br> admin/<br>fake_data/<int:count><br>product_table/<int:count>')
    #user/<br>order/<br>product/<br>user_order/<int:day>' 
    

def fake_data(request, count):
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
#------------------
def product_table(request, count):
    for i in range(1,count):
        product = Product.objects.get(id=i)
        print((f'ВЫВОД ТЕСТОВОЙ БАЗА ПРОДУКТОВ<br>i = {i}<br>product={product}<br>цена = {product.price}<br>количество = {product.quantity}<br>'))
        #return HttpResponse(f'ВЫВОД ТЕСТОВОЙ БАЗА ПРОДУКТОВ<br>i = {i}<br>product={product}<br>цена = {product.price}<br>количество = {product.quantity}<br>')
                            
        # total_price = {order.total_price}<br>product id = {product.id}<br><br>id ={Product.objects.get(id=randint(1, count*5))}<br>цена = {product.price}<br>количество = {product.quantity}<br>total_price = {order.total_price}<br>product id = {product.id}')  
        # # # #return render(request, 'basisapp/product_table.html', {'products': products})