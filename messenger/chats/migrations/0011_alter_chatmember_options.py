# Generated by Django 4.1.2 on 2022-10-30 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_alter_chatmember_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmember',
            options={'ordering': ['chat_id'], 'verbose_name': 'Участник чата', 'verbose_name_plural': 'Участники чата'},
        ),
    ]
