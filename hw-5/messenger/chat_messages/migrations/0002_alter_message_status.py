# Generated by Django 4.1.2 on 2022-10-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('NE', 'Not Delivered'), ('DE', 'Delivered'), ('RE', 'Read')], max_length=10, verbose_name='Статус сообщения'),
        ),
    ]
