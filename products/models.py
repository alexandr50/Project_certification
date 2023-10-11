from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    model = models.TextField(verbose_name='модель')
    release = models.DateField(verbose_name='дата выхода продукта на рынок')
    production_plant_prod = models.ForeignKey('production_plant.ProductionPlant',
                                              on_delete=models.PROTECT,
                                              verbose_name='завод',
                                              blank=True,
                                              null=True)
    retail_network_prod = models.ForeignKey('retail_network.RetailNetwork',
                                            on_delete=models.PROTECT,
                                            verbose_name='розничная сеть',
                                            blank=True, null=True)
    solo_trader_prod = models.ForeignKey('solo_trader.SoleTrader',
                                         on_delete=models.PROTECT,
                                         verbose_name='ип',
                                         blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
