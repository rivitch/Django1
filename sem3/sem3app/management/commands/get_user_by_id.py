"""
Если в базе несколько записей, вернёт одна, первая из результатазапроса
Если запись одна, first вернёт эту единственную запись
Если совпадений не найдено, вместо ошибки вернём None
"""

from django.core.management.base import BaseCommand
from lec2app.models import User

class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

# class Command(BaseCommand):
#     help = "Get user by id."

#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='User ID')

#     def handle(self, *args, **kwargs):
#         id = kwargs['id']
#         user = User.objects.get(id=id)
#         self.stdout.write(f'{user}')