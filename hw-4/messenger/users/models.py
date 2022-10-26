from django.db import models


# Models for user
class User(models.Model): # to AbstractUser
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор пользователя')
    phone_number = models.TextField(verbose_name='Номер телефона')
    username = models.TextField(unique=True, verbose_name='Имя пользователя')

    class Meta:
        verbose_name = 'Пользователь'


class UserInfo(models.Model): # UserProfile
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор записи о пользователе')
    name = models.TextField(verbose_name='Имя пользователя')
    info = models.TextField(verbose_name='Краткая информация о пользователе')
    creation_datetime = models.DateTimeField(verbose_name='Дата и время создания пользователя')
    user = models.OneToOneField(User, verbose_name='Идентификатор пользователя', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Информация о пользователе'
