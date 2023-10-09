from django.contrib import admin

from contacts.admin import ContactInline
from solo_trader.models import SoleTrader


@admin.register(SoleTrader)
class SoleTraderAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)

