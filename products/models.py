from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    model = models.TextField(verbose_name='модель')
    release = models.DateField(verbose_name='дата выхода продукта на рынок')
    production_plant_prod = models.ManyToManyField('production_plant.ProductionPlant',
                                                   verbose_name='завод',
                                                   blank=True)
    retail_network_prod = models.ManyToManyField('retail_network.RetailNetwork',
                                                 verbose_name='розничная сеть',
                                                 blank=True)
    solo_trader_prod = models.ManyToManyField('solo_trader.SoleTrader',
                                              verbose_name='ип',
                                              blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
