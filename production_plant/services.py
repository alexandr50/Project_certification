from django.contrib import admin

from contacts.models import Contact


class ContactCityFilter(admin.SimpleListFilter):

    title = 'City'
    parameter_name = 'contact__city'

    def lookups(self, request, model_admin):
        cities = Contact.objects.values_list('city', flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__city=self.value())
        return queryset
