from django.contrib import admin

from contacts.models import Contact


class ContactInline(admin.StackedInline):
    model = Contact


admin.site.register(Contact)
