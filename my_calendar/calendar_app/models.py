from __future__ import unicode_literals

from django.db import models

class Month(models.Model):
    title_month = models.CharField(max_length=150, verbose_name='Месяц')
    number_of_the_month = models.IntegerField(verbose_name='Номер по порядку')
    amount_of_days = models.IntegerField(verbose_name='Количество дней')

    def __str__(self):
        return self.title_month

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
        ordering = ['number_of_the_month']

class Week(models.Model):
    title_week = models.CharField(max_length=100, verbose_name='Неделя')
    number_of_the_week = models.IntegerField(verbose_name='Неделя')

    def __str__(self):
        return self.title_week

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'
        ordering = ['title_week']



