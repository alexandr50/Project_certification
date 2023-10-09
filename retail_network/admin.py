from django.contrib import admin
from retail_network.models import RetailNetwork


@admin.action(description='обнулить задолженность')
def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


class RetailNetworkAdmin(admin.ModelAdmin):
    list_filter = ('city',)
    actions = [clear_debt]


admin.site.register(RetailNetwork, RetailNetworkAdmin)

