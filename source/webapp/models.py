from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from django.utils import timezone


CATEGORY_CHOICES = (
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая Техника')
)

RAITING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.CharField(max_length=20, verbose_name='Категория',
                                choices=CATEGORY_CHOICES,default=None)
    descriptions = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE,
                               related_name='user_order', verbose_name='Автор')
    product = models.ForeignKey(Product, max_length=100, on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='products')
    review = models.TextField(max_length=3000, verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка', choices=RAITING_CHOICES, default=None)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


