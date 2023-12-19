#from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

"""
Поля модели «Клиент»:Client
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента
"""
class User(models.Model):
    first_name = models.CharField(max_length=10, help_text='Имя') # имя клиента
    last_name = models.CharField(max_length=100, help_text='Фамилия')
    email = models.EmailField()
    tel = models. TextField()
    adress = models. TextField()   #models.TextField()
    date_of_registration = models.DateField(null=True, blank=True)
    #orders = models.ManyToManyField(to='Order', blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email}'
        #return f'{self.last_name}, {self.first_name}'
    
"""Поля модели «Товар»:Product
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара    
"""

class Product(models.Model):
    #product = models.ForeignKey(max_length=100) # название товара
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=100) # описание товара
    #price = models.IntegerField() #(max_digits=8, decimal_places=2) # цена
    price = models.DecimalField(max_digits=8, decimal_places=2)              
    quantity = models.IntegerField() # количество
    date_add = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product} {self.price} {self.quantity} '

"""
Поля модели «Заказ»:Order
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    #product = models.ManyToManyField(Product)#,on_delete=models.CASCADE)
    #product = models.ManyToManyField(Product, on_delete=models.CASCADE)
    date_ordered = models.DateField(null=True, blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    # #total_price = models.IntegerField()
    
    # def product_return(self):
    #     """
    #     Creates a string for the Genre. This is required to display genre in Admin.
    #     """
    #     return ', '.join([ product.name for product in self.product.all() ])
    # product_return.short_description = 'Product'    
    
    def __str__(self):
        return f'{self.user} - {self.date_ordered}'
        #return f'{self.user} - {self.product} {self.date_ordered}'

# class MyModelName(models.Model):
#     """Типичный класс модели, производный от класса Model."""

#     # Поля
#     my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')
#     # …

#     # Метаданные
#     class Meta:
#         ordering = ['-my_field_name']

#     # Methods
#     def get_absolute_url(self):
#         """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
#         return reverse('model-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
#         return self.my_field_name
