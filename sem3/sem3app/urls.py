from django.urls import path
from . import views
"""
Импортируем уже знакомую функцию path и файл с представлениями из
текущего каталога (импорт через точку).
В данном примере мы определяем два маршрута: первый маршрут связывает
корневой URL с представлением index, а второй маршрут связывает URL
'/about/' с представлением about.
Функция path() принимает два аргумента: первый аргумент - это URL-адрес, а
второй - это представление, которое будет обрабатывать запрос на этот URL.
Также можно задать имя маршрута с помощью параметра name.
"""

urlpatterns = [
        path('', views.index),# name='index')#,product  order
        path('user/', views.user_name),# name='author_name'
        path('order/', views.order_name), # name='about'
        path('product/', views.product_name),
        ]