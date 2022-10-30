from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from users.models import User


# Models for chats and messages
class Chat(models.Model):
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
        verbose_name_plural = 'Чаты'

    class DoesNotExist(ObjectDoesNotExist):
        pass


class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        verbose_name='Идентификатор чата',
        on_delete=models.CASCADE,
        related_name='chat_members'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Идентификатор пользоателя',
        on_delete=models.CASCADE,
        related_name='chat_members'
    )
    datetime_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время добавления в чат'
    )

    class Meta:
        verbose_name = 'Участник чата'
        verbose_name_plural = 'Участники чата'
        unique_together = ('chat', 'user')
