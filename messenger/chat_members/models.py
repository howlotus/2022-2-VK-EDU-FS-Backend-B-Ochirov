from django.db import models
from chats.models import Chat
from users.models import User


# Create your models here.
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
        ordering = ['chat_id']
