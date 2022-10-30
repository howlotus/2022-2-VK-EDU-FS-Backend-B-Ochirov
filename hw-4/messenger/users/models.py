from django.db import models
from django.contrib.auth.models import AbstractUser


# Models for user
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=16,
        verbose_name='Номер телефона'
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Уникальное имя пользователя'
    )

    class Meta:
        verbose_name = 'Пользователь'


class UserProfile(models.Model):  # UserProfile
    full_name = models.CharField(
        max_length=50,
        verbose_name='Полное имя пользователя'
    )
    info = models.CharField(
        max_length=120,
        verbose_name='Краткая информация о пользователе'
    )
    user = models.OneToOneField(
        User,
        verbose_name='Идентификатор пользователя',
        on_delete=models.CASCADE,
        related_name='user_profiles'
    )

    class Meta:
        verbose_name = 'Информация о пользователе'
