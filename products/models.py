from django.db import models

#Создаю класс (таблицу) товаров 
#Она должна наследоваться от models.Model
class Product (models.Model):
    # Поле id создается само, нам писать ничего не надо
    # verbose_name человеческое имя, которое будет отображаться в административной панеле
    # max_length максимальная длина строки. только для CharField
    title = models.CharField(verbose_name="Название товара", max_length=150)
    price = models.FloatField(verbose_name="Цена")
    desc = models.TextField(verbose_name="Описание товара")

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    # Чтобы в списке на административной панели товары отображались под своими названиями 
    def __str__(self):
        return self.title

# команда py manage.py makemigrations - создание миграции для создания таблицы
# команда py manage.py migrate добавление таблицы