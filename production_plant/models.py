from django.db import models


class ProductionPlant(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    email = models.CharField(max_length=30, verbose_name='почта', unique=True)
    country = models.CharField(max_length=30, verbose_name='страна')
    city = models.CharField(max_length=30, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    number_home = models.CharField(max_length=10, verbose_name='номер дома')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'
