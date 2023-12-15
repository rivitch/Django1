from django.core.management.base import BaseCommand
from random import *
from viewsapp.models import Order, User, Product

class Command(BaseCommand):
    help = "Update user name by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        #parser.add_argument('name', type=str, help='User name')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        count = kwargs.get('count')
        user = User.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=pk).first()
        for i in range(1, count + 1):
            order = Order(user=f'Name{user}', product=f'Product = {product}', date_ordered = '{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}', total_price = {int(Product.price)*Product.quantity}, is_deleted=f'{0}')
            order.save()
        order.user = user
        order.save()
        self.stdout.write(f'{order}')
        
# #-----------       
# class Command(BaseCommand):
#     help = "Generate fake Orders."
#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int, help='Order ID')
#     def handle(self, *args, **kwargs):
#         count = kwargs.get('count')
#         x = 1
#         y = randint(000, 999)
#         for i in range(1, count + 1):
#             order = Order(name=f'Name{y}', email=f'mail{y}@mail.ru', password=f'{x}', age=f'{randint(18, 100)}', is_deleted=f'{0}')
#             order.save()