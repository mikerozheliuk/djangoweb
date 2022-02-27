from django.db import models


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Назва статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        # verbose_name = 'Закази'

class ComentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='текст коментарія')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата створення')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Коментарій'
        # verbose_name = 'Заказ
