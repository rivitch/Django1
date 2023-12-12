import logging
              
from random import * # import random
from django.shortcuts import render
#from django.shortcuts import get_object_or_404
from django.http import HttpResponse


#from .models import User, Product, Order
#from django.views import View

logger = logging.getLogger(__name__)

def index(request):
    logger.info('BASIS page accessed')
    return HttpResponse(f'ВЫ НА ГЛАВНОЙ СТРАНИЦЕ DJANGO<br><br>Используя URLconf, определенный в basisapp.urls, Django попробовал эти шаблоны URL в следующем порядке:<br> admin/<br>user/<br>order/<br>product/<br>user_order/<int:day>' 
    )

# def user_name(request, count):
#     for i in range(count):
#         user = User(first_name=f'Имя {randint(000, 999)}', last_name=f'Фамилия {randint(000, 999)}', email=f'{randint(000, 999)}@mail.ru', tel=f'+7800{randint(1111111, 9999999)}', adress=f'Адрес {randint(000, 999)}', date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
#         user.save()
#     logger.info('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')
#     return HttpResponse('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')

# def product_name(request, count):
#     for i in range(count):
#         product = Product(product=f'Товар {randint(000, 999)}', description=f'Описание {randint(000, 999)}',  price=f'{randint(1, 10)}', quantity=f'{randint(1, 100)}', date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
#         product.save()
#     logger.info('ОБНОВЛЕНА БАЗА ТОВАРОВ')   
#     return HttpResponse('ОБНОВЛЕНА БАЗА ТОВАРОВ')

# def user_order(request,id, days):
#     user = get_object_or_404(User, pk=User.id)
#     order = Order.objects.filter(user=user).order_by('-id')[:days]
#     return render(request, "sem3app/index_sem3app.html", {'user': user, 'order': order})

# def order_name(request):
#     order=Order(user=User.objects.first(),
#         date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}', 
#         total_price=f'{int(Product.price)*Product.quantity}') #str((int(Product.price))*(int(Product.quantity)))
#         #total_price=str((int(Product.price))*(int(Product.quantity))))
#     order.save()
#     logger.info('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')   
#     return HttpResponse('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')  



