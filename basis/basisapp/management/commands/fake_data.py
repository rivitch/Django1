from django.core.management.base import BaseCommand
from random import *
from basisapp.models import User #Author, Post

class Command(BaseCommand):
    help = "Generate fake User."# and posts."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        x = 1
        y = randint(000, 999)
        for i in range(1, count + 1):
            user = User(name=f'Name{y}', email=f'mail{y}@mail.ru', password=f'{x}', age=f'{randint(18, 100)}', is_deleted=f'{0}')
            user.save()
    #                    password = models.CharField(max_length=100)
    # age = models.IntegerField()
    # is_deleted = models.BooleanField(default=False) 
    #              user = User(first_name=f'Имя {randint(000, 999)}', last_name=f'Фамилия {randint(000, 999)}', email=f'{randint(000, 999)}@mail.ru', tel=f'+7800{randint(1111111, 9999999)}', adress=f'Адрес {randint(000, 999)}', date_of_registration=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')   
        # for j in range(1, count + 1):
        #     post = Post(title=f'Title{j}', content=f'Text from {author.name} #{j} is bla bla bla many long text', author=author)
        #     post.save()