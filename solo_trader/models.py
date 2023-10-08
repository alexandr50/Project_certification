from django.db import models


class SoleTrader(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')
    supplier_pd = models.ForeignKey('production_plant.ProductionPlant',
                                    on_delete=models.PROTECT,
                                    verbose_name='поставщик завод',
                                    blank=True,
                                    null=True)
    supplier_rt = models.ForeignKey('retail_network.RetailNetwork',
                                    on_delete=models.PROTECT,
                                    verbose_name='поставщик розничная сеть',
                                    blank=True,
                                    null=True
                                    )

    debt = models.FloatField(default=0, verbose_name='задолженность')

    def __str__(self):
        return self.title

    def clean(self):
        if self.supplier_pd and self.supplier_rt:
            raise ValueError('Выберите только одного поставщика')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Индивидуальный пердприниматель'
        verbose_name_plural = 'Индивидуальныйе пердприниматели'
