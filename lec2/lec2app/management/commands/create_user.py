from django.core.management.base import BaseCommand
from lec2app.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=25) 
        user.save()
        self.stdout.write(f'{user}')
    # def user_name(request):
    #     for i in range(1):
    #         user = User(first_name=f'Имя {randint(000, 999)}', last_name=f'Фамилия {randint(000, 999)}', email=f'{randint(000, 999)}@mail.ru', tel=f'+7800{randint(1111111, 9999999)}', adress=f'Адрес {randint(000, 999)}', date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
    #         user.save()
    #     return HttpResponse('ОБНОВЛЕНА БАЗА КЛИЕНТОВ')
