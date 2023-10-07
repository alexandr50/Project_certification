from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    model = models.TextField(verbose_name='модель')
    release = models.DateField(verbose_name='дата выхода продукта на рынок')
    production_plant = models.ForeignKey('production_plant.ProductionPlant',
                                         on_delete=models.PROTECT,
                                         verbose_name='завод')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
