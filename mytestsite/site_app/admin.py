from django.contrib import admin

# Register your models here.
from .models import User, Product, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'tel', 'adress', 'date_of_registration', 'is_deleted')
    pass

admin.site.register(User, UserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'price', 'quantity', 'date_add', 'image', 'is_deleted')
    pass

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date_ordered', 'product_price', 'total_price', 'is_deleted')
    pass

admin.site.register(Order, OrderAdmin)
#class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'date_ordered', 'total_price', 'is_deleted')
#     pass

# admin.site.register(Order, OrderAdmin)
#admin.site.register(Order)
