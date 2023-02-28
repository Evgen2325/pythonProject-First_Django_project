from django.db import models


class Bills(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена', default=0)
    date = models.DateField('Дата')

    def __str__(self):
        return f'{self.date:%Y-%m-%d}{self.price:->30}р.{self.title:->30}'

    def get_absolute_url(self):
        return f'/bills/{self.id}'

    class Meta:
        verbose_name = 'Расчёт'
        verbose_name_plural = 'Расчёты'
