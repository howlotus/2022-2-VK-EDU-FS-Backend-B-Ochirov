from django.db import models
from users.models import User


# Models for chats and messages
class Chat(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(
        max_length=30,
        verbose_name='Название чата'
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания чата'
    )

    class Meta:
        verbose_name = 'Чат'


class Message(models.Model):
    DELIVERED = 'DE'
    READ = 'RE'
    MESSAGE_STATUS = [
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


class ChatMember(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Идентификатор пользоателя',
        on_delete=models.CASCADE,
        related_name='chat_members'
    )
    chat = models.ForeignKey(
        Chat,
        verbose_name='Идентификатор чата',
        on_delete=models.CASCADE,
        related_name='chat_members'
    )
    datetime_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время добавления в чат'
    )

    class Meta:
        verbose_name = 'Участник чата'
        unique_together = ('user', 'chat',)
