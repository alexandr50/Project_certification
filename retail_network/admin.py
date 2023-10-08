from django.contrib import admin

from retail_network.models import RetailNetwork


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    pass

