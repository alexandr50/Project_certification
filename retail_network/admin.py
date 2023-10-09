from django.contrib import admin

from contacts.admin import ContactInline
from production_plant.services import ContactCityFilter
from retail_network.models import RetailNetwork


@admin.action(description='обнулить задолженность')
def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)
    list_filter = ('title', ContactCityFilter,)
    actions = [clear_debt]
