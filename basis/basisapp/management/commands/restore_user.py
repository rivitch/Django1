from django.core.management.base import BaseCommand
from basisapp.models import User

class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.is_deleted = False
            user.save()
            #user.delete()
        self.stdout.write(f'{user}')

#-----

# class Command(BaseCommand):
#     help = "Restore user name by id."
#     def add_arguments(self, parser):
#         parser.add_argument('pk', type=int, help='User ID')
#         parser.add_argument('is_deleted', type=int, help='is_deleted')
#     def handle(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         name = kwargs.get('name')
#         user = User.objects.filter(pk=pk).first()
#         user.name = name
#         user.save()
#         self.stdout.write(f'{user}')