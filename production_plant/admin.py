from django.contrib import admin


from contacts.admin import ContactInline
from .models import ProductionPlant


@admin.register(ProductionPlant)
class ProductionPlantAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)
