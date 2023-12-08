#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# Задание №1. Создайте модель для запоминания бросков монеты: орёл или решка. Также запоминайте время броска (модуль coin)
# Задание №3. Создайте модель Автор. Модель должна содержать следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создайте пользовательское поле “полное имя”, которое возвращает имя и фамилию.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sem2.settings')
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
