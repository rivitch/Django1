from django.urls import path
from . import views
# Sem3
from .views import helloView, HelloView

from .views import year_post, MonthPost, post_detail, my_view, view_client
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
        path('hello/', helloView, name='hello'),# указываем имя функции в качестве обработчика запроса
        path('hello2/', HelloView.as_view(), name='hello2'),#используем метод as_view() класса! HelloView для создания объекта-обработчика запроса
        path('user_year/<int:year>/', year_post, name='year_post'),
        path('my_view/', my_view, name='my_view'),
        path('client/<int:day>/',view_client,name='client'),

        ]