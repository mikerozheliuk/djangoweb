from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат айди ')
    tg_message = models.TextField(verbose_name='Текстове повідомлення')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройка'
