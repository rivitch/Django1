from django.core.management.base import BaseCommand
from basisapp.models import User

class Command(BaseCommand):
    help = "Update user name by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('last_name', type=str, help='last_name')
        parser.add_argument('email', type=str, help='email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        last_name = kwargs.get('last_name')
        email = kwargs.get('email')
        user = User.objects.filter(pk=pk).first()
        user.first_name = name
        user.last_name = last_name
        user.email = email
        #first_name
        user.save()
        self.stdout.write(f'{user}')