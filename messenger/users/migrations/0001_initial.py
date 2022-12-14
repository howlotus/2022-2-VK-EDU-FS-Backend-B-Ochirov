# Generated by Django 4.1.2 on 2022-10-25 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор пользователя')),
                ('phone_number', models.TextField(verbose_name='Номер телефона')),
                ('username', models.TextField(unique=True, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор записи о пользователе')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
                ('info', models.TextField(verbose_name='Краткая информация о пользователе')),
                ('creation_datetime', models.DateTimeField(verbose_name='Дата и время создания пользователя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Идентификатор пользователя')),
            ],
            options={
                'verbose_name': 'Информация о пользователе',
            },
        ),
    ]
