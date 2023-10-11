from django.http import Http404
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.db import IntegrityError
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from production_plant.models import ProductionPlant
from products.models import Product
from products.serializers import ProductSerializer


class ProductionPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlant
        fields = ('title',)


class ProductionPlantCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True, required=False)

    def create(self, validated_data):
        data_for_contact = validated_data.pop('contact')
        data_for_prod_pl = validated_data.pop('title')
        data_for_product = validated_data.pop('products')
        prod_plant = ProductionPlant.objects.create(title=data_for_prod_pl)
        Contact.objects.create(**data_for_contact, production_plant=prod_plant)
        for prod in data_for_product:
            Product.objects.create(**prod)

        return prod_plant



    class Meta:
        model = ProductionPlant
        fields = ('title', 'contact', 'products')

class ProductionPlantUpdateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        new_email = validated_data.get('contact').get('email')
        new_country = validated_data.get('contact').get('country')
        new_city = validated_data.get('contact').get('city')
        new_street = validated_data.get('contact').get('street')
        new_number_home = validated_data.get('contact').get('number_home')
        instance.contact.email = new_email
        instance.contact.country = new_country
        instance.contact.city = new_city
        instance.contact.street = new_street
        instance.contact.number_home = new_number_home
        instance.contact.production_plant_id = validated_data.get("contact.production_plant_id",
                                                                  instance.contact.production_plant_id)
        instance.save()
        return instance

    class Meta:
        model = ProductionPlant
        fields = ('title', 'contact')