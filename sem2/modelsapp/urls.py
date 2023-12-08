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
        #path('', views.index, name='index'),
        #path('about/', views.about, name='about'),
        #path('', views.game_coin, name='game_coin'),
        path('author/', views.author_name),# name='author_name'
        ]