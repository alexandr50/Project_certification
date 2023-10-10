from django.contrib import admin

from contacts.admin import ContactInline
from .models import ProductionPlant
from .services import ContactCityFilter


@admin.register(ProductionPlant)
class ProductionPlantAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)
    list_filter = ('title', ContactCityFilter,)

