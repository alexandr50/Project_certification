from django.contrib import admin

from solo_trader.models import SoleTrader


@admin.register(SoleTrader)
class SoleTraderAdmin(admin.ModelAdmin):
    pass

