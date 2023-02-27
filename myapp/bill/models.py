from django.db import models


class Bills(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена', default=0)
    date = models.DateTimeField('Дата')

    def __str__(self):
        return f' {self.title}           {self.price}р.           {self.date}'

    class Meta:
        verbose_name = 'Расчёт'
        verbose_name_plural = 'Расчёты'
