from django.db import models


class Rate(models.Model):
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
