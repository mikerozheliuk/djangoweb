from django.db import models


# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=200, verbose_name='Ціна')
    pc_description = models.CharField(max_length=200, verbose_name='Описання')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Ціна'
        # verbose_name = 'Закази'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Послуга')
    pt_old_price = models.CharField(max_length=200, verbose_name='Стара ціна')
    pt_new_price = models.CharField(max_length=200, verbose_name='Нова ціна')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Послуги'
        # verbose_name = 'Закази'
