from django.contrib import admin


from products.admin import ContactInline
from .models import ProductionPlant


@admin.register(ProductionPlant)
class BankCardAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)
