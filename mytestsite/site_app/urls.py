from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('', views.index),
    #path('',index,name='title'),
    path('fake_data/<int:count>', views.fake_data),
    path('fake_data_order/<int:count>', views.fake_data_order),
    path('production/<int:count>', views.production),
    

]