"""
Конфигурация URL-адреса для проекта myproject.

Список urlpatterns направляет URL-адреса к представлениям. Для получения дополнительной информации, пожалуйста, смотрите:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Примеры:
Функциональные представления
    1. Добавьте импорт: из my_app представления импорта
    2. Добавьте URL-адрес в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: из other_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируем функцию include(): из django.urls import include, path
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('prefix/', include('myapp.urls')),
]
