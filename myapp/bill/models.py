from django.db import models


class Bills(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена', default=0)
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расчёт'
        verbose_name_plural = 'Расчёт'