from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


TOKEN_TYPE_REGISTER = 'register'
TOKEN_TYPE_PASSWORD_RESET = 'password_reset'
TOKEN_TYPE_CHOICES = (
    (TOKEN_TYPE_REGISTER, 'Регистрация'),
    (TOKEN_TYPE_PASSWORD_RESET, 'Восстановление пароля')
)


class Profile(models.Model):
    user: AbstractUser = models.OneToOneField(get_user_model(), related_name='profile',
                                              on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
