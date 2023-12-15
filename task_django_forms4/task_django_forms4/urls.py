
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_django_forms4app.urls')),
    path('forms4app/', include('task_django_forms4app.urls')),
]
