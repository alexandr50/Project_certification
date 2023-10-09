from django.contrib import admin

from contacts.admin import ContactInline
from retail_network.models import RetailNetwork


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)

