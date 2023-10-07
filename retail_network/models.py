from django.db import models


class RetailNetwork(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')
    supplier = models.ManyToManyField('production_plant.ProductionPlant', verbose_name='поставщик')
    debt = models.FloatField(default=0, verbose_name='задолженность')

