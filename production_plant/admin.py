from django.contrib import admin



from .models import ProductionPlant


@admin.register(ProductionPlant)
class ProductionPlantAdmin(admin.ModelAdmin):
    list_filter = ('city',)

