from django.db import models

from contacts.models import Contact


class ProductionPlant(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    created_at = models.TimeField(auto_now_add=True, verbose_name='время создания')

    def save(self, *args, **kwargs):
        try:
            city = self.contact.city
            country = self.contact.country
            email = self.contact.email
            street = self.contact.street
            number_phone = self.contact.number_home
        except:
            raise ValueError('Необходимо добавить контактную информацию')
        else:
            super().save(*args, *kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'
