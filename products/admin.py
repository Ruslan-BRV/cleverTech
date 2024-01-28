from django.contrib import admin
from products.models import Product

# Добавляем нашу таблицу товаров на административную панель
admin.site.register(Product)

# Чтобы зайти на административную панель, нужен суперадмин, которого нужно создать
# py manage.py createsuperuser