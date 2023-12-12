from django.core.management.base import BaseCommand
from viewsapp.models import User

class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')

# read


# update
# class Command(BaseCommand):
#     help = "Update user."
#     def handle(self, *args, **kwargs):
#         user = User.objects.first()
#         user.name = 'John'
#         user.save()
#         self.stdout.write(f'{user}')
#     # def user_name(request):
#     #     for i in range(1):

#  delete

# read

