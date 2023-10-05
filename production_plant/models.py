from django.db import models

class ProductionPlant(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'
