#from django.shortcuts import render

# Create your views here.
import logging
from django.shortcuts import render
from .forms import UserForm

logger = logging.getLogger(__name__)
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        age = form.cleaned_data['age']
        # Делаем что-то с данными
        logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'lec4app/user_form.html', {'form': form})