from django.db import models

#Create your models here.



"""
Поля модели «Клиент»:Client
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента
"""
class User(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100) # имя клиента
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models. TextField()
    adress = models. TextField()   #models.TextField()
    date_of_registration = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.last_name}, {self.first_name}'
    
"""Поля модели «Товар»:Product
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара    
"""

class Product(models.Model):
    product = models.CharField(max_length=100) # название товара
    description = models.CharField(max_length=100) # описание товара
    price = models.IntegerField() #(max_digits=8, decimal_places=2) # цена              
    quantity = models.IntegerField() # количество
    date_add = models.DateField(null=True, blank=True)
    def __str__(self):
        return f'{self.name} {self.price} {self.quantity}'

"""
Поля модели «Заказ»:Order
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""
class Order(models.Model):
    user = models.ForeignKey(to='User',on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product',on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(null=True, blank=True)
    total_price = models.IntegerField()
    def __str__(self):
        return f'{self.product} {self.date_ordered}'
