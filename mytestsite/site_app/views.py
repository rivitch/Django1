from django.shortcuts import render

# Create your views here.
import logging
from random import *
from django.http import HttpResponse
from .models import User, Product, Order

logger = logging.getLogger(__name__)

def index(request):
    logger.info('BASIS page accessed')
    return HttpResponse(f'ВЫ НА ГЛАВНОЙ СТРАНИЦЕ (DJANGO)<br><br>Используя URLconf, определенный в site_app.urls, Django попробовал эти шаблоны URL в следующем порядке:<br> admin/<br>fake_data/число<br>production/число<br>')
    #user/<br>order/<br>product/<br>user_order/<int:day>' 
# path('fake_data/<int:count>', views.fake_data),
   # path('production/<int:count>', views.production),
  # path('', views.index),

def fake_data(request, count):   # заполняем тестовую базу
    #x = 1  # if needed password
    for i in range(count):
        y = randint(111, 999)
        product = Product(product=f'Товар{y}', 
                          description=f'Описание {y}',  
                          price=randint(1, 10), 
                          quantity=randint(1, 100), 
                          date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
                          image=f'img{y}.jpg',
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
    logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА КЛИЕНТОВ')
    #x = {Product.objects.get(id=randint(1, 3))}
    return HttpResponse(f'ОБНОВЛЕНА БАЗА ТОВАРОВ И КЛИЕНТОВ<br><br><br>product.price = {Product.objects.get(id=randint(1, 3)).price}<br>')#id ={x.id}  product.quantity = {x.quantity} 


def production(request,count):
    #product = Product.objects.get(id=randint(1,count*2))
    logger.info('ВЫ НА СТРАНИЦЕ ПРОДУКЦИИ (DJANGO)')
    #return HttpResponse(f'ВЫ НА СТРАНИЦЕ ПРОДУКЦИИ (DJANGO)<br><br>id ={Product.objects.get(price)}')
    #list_x = []
    x=Product.objects.get(id=randint(1, count))
    #list_x.append(x)
    #return {x}
    return HttpResponse(f'ВЫ НА СТРАНИЦЕ ПРОДУКЦИИ (DJANGO)<br><br>id ={x}<br>цена = {x.price}<br>количество = {x.quantity}<br>')#list_x = {list_x}')
    
    # for i in range(count):
    #     y = randint(111, 999)
    #         #x = randint(1, count*5)
    #     order=Order(user=User.objects.get(id=randint(1,3)),
    #                     #user = users,
    #                     product = Product.objects.get(id=randint(1,3)),
    #                     #product = product,
    #                     #product = Product.objects.get(id=randint(1,count*2)),
    #                     #product_price = Product.objects.get(product.price),
    #                     date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
    #                     total_price=product.price*product.quantity,
    #                     #total_price=product.price*product.quantity,
    #                     is_deleted=f'{0}',
    #                     )
    #     order.save()
    # logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА ЗАКАЗОВ<br><br>product.price = {product.price}<br>product.quantity = {product.quantity}')
 
    # return HttpResponse(f'ОБНОВЛЕНА БАЗА ЗАКАЗОВ<br><br>product.price = {product.price}<br>product.quantity = {product.quantity}')#<br>y = {y}<br>user={users}<br>product={product}<br>цена = {product.price}<br>количество = {product.quantity}<br>total_price = {order.total_price}<br>product id = {product.id}<br><br>id ={Product.objects.get(id=randint(1, count*5))}<br>цена = {product.price}<br>количество = {product.quantity}<br>total_price = {order.total_price}<br>product id = {product.id}')

def fake_data_order(request, count):   # заполняем тестовую базу
    for i in range(count):
        y = randint(111, 999)
            #x = randint(1, count*5)
        #x=production(request,count)
        x=Product.objects.get(id=randint(1, count))
        order=Order(user=User.objects.get(id=randint(1,3)),
                        #user = users,
                        #product = Product.objects.get(id=randint(1,3)),
                        #product = product,
                        product = x,
                        #product = Product.objects.get(id=randint(1,count*2)),
                        product_price = x.price,
                        #product_price = Product.objects.get(product.price),
                        date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}',
                        total_price=x.price*x.quantity,
                        #total_price=product.price*product.quantity,
                        is_deleted=f'{0}',
                        )
        order.save()
    logger.info('ОБНОВЛЕНА ТЕСТОВАЯ БАЗА ЗАКАЗОВ<br><br>product.price = {product.price}<br>product.quantity = {product.quantity}')
 
    return HttpResponse(f'ОБНОВЛЕНА БАЗА ЗАКАЗОВ<br><br>product.price = {x.price}<br>product.quantity = {x.quantity}')
    pass
