from django.shortcuts import render, get_object_or_404
import logging
# Create your views here.
from django.http import HttpResponse

from random import *
from .models import User, Product, Order
# Sem3
from django.views import View




logger = logging.getLogger(__name__)

# def helloView(request):
#     logger.info('helloView def page accessed')
#     return HttpResponse('Hello World from function!') 

# class HelloView(View):
#     def get(self, request):
#         logger.info('HelloView class page accessed')
#         return HttpResponse("Hello World from class!")
    
# def year_post(request, year):        # Представление через функцию возвращает HttpResponse
#     text = "sdgfhgjhkj"
#     ... # формируем статьи за год
#     return HttpResponse(f"Posts from {year}<br>{text}")

# # Представление через класс возвращает HttpResponse
# class MonthPost(View):
#     def get(self, request, year, month):
#         text = "123456789"
#         ... # формируем статьи за год и месяц
#         return HttpResponse(f"Posts from {month}/{year}<br>{text}")
    
# # Представление через функцию возвращает JSON    
# from django.http import JsonResponse

# def post_detail(request, year, month, slug):
#     # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
#     post = {
#         "year": year,
#         "month": month,
#         "slug": slug,
#         "title": "Кто быстрее создаёт списки в Python, list() или []",
#         "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
#         }
#     return JsonResponse(post, json_dumps_params={'ensure_ascii': False}) # текст в кодировке UTF-8, а не в ASCII


def index(request):
    logger.info('DJANGO_SEM3 page accessed')
    return HttpResponse(f'ВЫ НА СТРАНИЦЕ СЕМИНАРА 3. DJANGO<br>Using the URLconf defined in sem3.urls, Django tried these URL patterns, in this order:<br> admin/<br>user/<br>order/<br>product/<br>user_order/<int:day>' 
    )

def user_name(request, count):
    for i in range(count):
        user = User(first_name=f'Имя {randint(000, 999)}', 
                    last_name=f'Фамилия {randint(000, 999)}', 
                    email=f'{randint(000, 999)}@mail.ru', 
                    tel=f'+7800{randint(1111111, 9999999)}', 
                    adress=f'Адрес {randint(000, 999)}', 
                    date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        user.save()
    logger.info('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')
    return HttpResponse('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')

def product_name(request, count):
    for i in range(count):
        product = Product(product=f'Товар {randint(000, 999)}', description=f'Описание {randint(000, 999)}',  price=f'{randint(1, 10)}', quantity=f'{randint(1, 100)}', date_add=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
        product.save()
    logger.info('ОБНОВЛЕНА БАЗА ТОВАРОВ')   
    return HttpResponse('ОБНОВЛЕНА БАЗА ТОВАРОВ')

def user_order(request,id, days):#, days
    user = get_object_or_404(User, pk=id)
    logger.info('User.id = {User.id}')
    order = Order.objects.filter(user=user).order_by('-id')[:days]
    if not order:
        return HttpResponse(f'Пользователь = {user},<br>Заказов за {days} дня(дней) нет')
    return render(request, "viewsapp/index_viewsapp.html", {'user': user, 'order': order})
    #return HttpResponse(f'Пользователь = {user},<br>Заказов за {days} дня(дней) = {order}')

def order_name(request, count):
    for i in range(count):
        order=Order(user=User.objects.first(),product = Product.objects.first(),
        date_ordered=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}', 
        total_price=f'{Product.price*Product.quantity}') #str((int(Product.price))*(int(Product.quantity)))
        #total_price=str((int(Product.price))*(int(Product.quantity))))
    order.save()
    logger.info('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')   
    return HttpResponse('ОБНОВЛЕНА БАЗА ЗАКАЗОВ')  


# def my_view(request):
#     context = {"name": "John"}
#     return render(request, "sem3app/index_sem3app.html", context)

# def view_client(requests,day_):
#     context = {"name": "John"}
#     return render(requests, "sem3app/product.html", context)