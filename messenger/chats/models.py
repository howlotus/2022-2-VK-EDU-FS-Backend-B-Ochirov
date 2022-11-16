from django.db import models


# Models for chats and messages
class Chat(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Название чата'
    )
    description = models.CharField(
        max_length=50,
        verbose_name='Описание чата'
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания чата'
    )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
