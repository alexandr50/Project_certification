from django.db import models


class RetailNetwork(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    email = models.CharField(max_length=30, verbose_name='почта', unique=True)
    country = models.CharField(max_length=30, verbose_name='страна')
    city = models.CharField(max_length=30, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    number_home = models.CharField(max_length=10, verbose_name='номер дома')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')
    supplier = models.ForeignKey('production_plant.ProductionPlant',
                                 default=None,
                                 on_delete=models.PROTECT,
                                 verbose_name='поставщик')
    debt = models.FloatField(default=0, verbose_name='задолженность')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

