from django.contrib import admin


from solo_trader.models import SoleTrader



@admin.action(description='clear_debt')
def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


class SoleTraderAdmin(admin.ModelAdmin):
    list_filter = ('city',)
    actions = [clear_debt]

admin.site.register(SoleTrader, SoleTraderAdmin)


