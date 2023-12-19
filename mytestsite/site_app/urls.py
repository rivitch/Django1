from django.urls import path
from . import views


urlpatterns = [
    path('fake_data/<int:count>', views.fake_data),
    path('fake_data_order/<int:count>', views.fake_data_order),
    path('production/<int:count>', views.production),
    path('', views.index),

]