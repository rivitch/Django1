from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
from random import *
from .models import User, Product, Order

logger = logging.getLogger(__name__)

def index(request):
    logger.info('DJANGO_SEM3 page accessed')
    return HttpResponse('ВЫ НА СТРАНИЦЕ СЕМИНАРА 3. DJANGO  Using the URLconf defined in sem3.urls, Django tried these URL patterns, in this order: admin/   или  sem3app/user/   или  sem3app/order/   или  sem3app/product/' 
    # return HttpResponse('ВЫ НА СТРАНИЦЕ СЕМИНАРА 3.' 
    # DJANGO  Using the URLconf defined in sem3.urls, Django tried these URL patterns, in this order:'
    # admin/
    # sem3app/ user/
    # sem3app/ order/
    # sem3app/ product/
)

def user_name(request):
    for i in range(3):
        user = User(first_name=f'Имя {randint(000, 999)}', last_name=f'Фамилия {randint(000, 999)}', email=f'{randint(000, 999)}@mail.ru', tel=f'+7800{randint(1111111, 9999999)}', adress=f'Адрес {randint(000, 999)}', date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        user.save()
    logger.info('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')
    return HttpResponse('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')

def product_name(request):
    for i in range(10):
        product = Product(product=f'Товар {randint(000, 999)}', description=f'Описание {randint(000, 999)}',  price=f'{randint(1, 10)}', quantity=f'{randint(1, 100)}', date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        product.save()
    logger.info('ОБНОВЛЕНА БАЗА ТОВАРОВ')   
    return HttpResponse('ОБНОВЛЕНА БАЗА ТОВАРОВ')

def order_name(request):
    order=Order(user=User.objects.first(),
        date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}', 
        total_price=f'{int(Product.price)*Product.quantity}') #str((int(Product.price))*(int(Product.quantity)))
        #total_price=str((int(Product.price))*(int(Product.quantity))))
    order.save()
    logger.info('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')   
    return HttpResponse('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')  