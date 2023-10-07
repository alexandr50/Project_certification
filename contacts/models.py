from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=30, verbose_name='почта')
    country = models.CharField(max_length=30, verbose_name='страна')
    city = models.CharField(max_length=30, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    number_home = models.CharField(max_length=10, verbose_name='номер дома')
    production_plant = models.OneToOneField('production_plant.ProductionPlant',
                                            on_delete=models.CASCADE,
                                            verbose_name='завод',
                                            blank=True, null=True)
    retail_network = models.OneToOneField('retail_network.RetailNetwork',
                                          on_delete=models.CASCADE,
                                          verbose_name='розничная сеть',
                                          blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
