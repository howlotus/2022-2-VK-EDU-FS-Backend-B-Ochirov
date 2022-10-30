from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from users.models import User
from chats.models import Chat


# Create your models here.
class Message(models.Model):
    objects = None
    NOT_DELIVERED = 'NE'
    DELIVERED = 'DE'
    READ = 'RE'
    MESSAGE_STATUS = [
        (NOT_DELIVERED, 'Not Delivered'),
        (DELIVERED, 'Delivered'),
        (READ, 'Read')
    ]

    chat = models.ForeignKey(
        Chat,
        null=True,
        verbose_name='Идентификатор чата',
        on_delete=models.SET_NULL,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User,
        null=True,
        verbose_name='Идентификатор отправителя',
        on_delete=models.SET_NULL,
        related_name='messages'
    )
    content = models.TextField(verbose_name='Сообщение')
    datetime_sent = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время сообщения'
    )
    status = models.CharField(
        max_length=10,
        choices=MESSAGE_STATUS,
        verbose_name='Статус сообщения'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['chat_id']

    class DoesNotExist(ObjectDoesNotExist):
        pass
