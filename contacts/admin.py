from django.contrib import admin

from contacts.models import Contact


class ContactInline(admin.StackedInline):
    model = Contact
    list_display = ('email', 'country', 'city', 'street', 'number_home')


admin.site.register(Contact)
