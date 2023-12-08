#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
Задание

Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:Product
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:Order
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

    Допишите несколько функций CRUD для работы с моделями по желанию. 
"""
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_django_models2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
