from django.db import models
from django.utils.timezone import now
from users.models import User


# Create your models here.
class Chat(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор чата')
    first_user = models.ForeignKey(User, default=1, verbose_name='Идентификатор пользователя 1',
                                   on_delete=models.PROTECT)
    creation_datetime = models.DateTimeField(default=now, verbose_name='Дата и время создания чата')

    class Meta:
        verbose_name = 'Чат'


class Message(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор сообщения')
    chat = models.ForeignKey(Chat, default=1, verbose_name='Идентификатор чата', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, default=2, verbose_name='Идентификатор отправителя', on_delete=models.CASCADE)
    message_text = models.TextField(verbose_name='Сообщение')
    datetime = models.DateTimeField(verbose_name='Дата и время сообщения')
    status = models.SmallIntegerField(verbose_name='Статус прочитанности сообщения')

    class Meta:
        verbose_name = 'Сообщение'
