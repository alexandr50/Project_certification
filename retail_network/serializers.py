from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from production_plant.models import ProductionPlant
from production_plant.serializers import ProductionPlantSerializer, ProductionPlantCreateSerializer

from retail_network.models import RetailNetwork


class RetailNetworkForSoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = ('title',)


class RetailNetworkSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    supplier = ProductionPlantSerializer()

    class Meta:
        model = RetailNetwork
        fields = ('title', 'contact', 'supplier')


class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    supplier = ProductionPlantSerializer()

    def create(self, validated_data):
        data_for_contact = validated_data.pop('contact')
        data_for_retail_nw = validated_data.pop('title')
        data_for_prod_pl = validated_data.pop('supplier').pop('title')
        try:
            prod_pl = get_object_or_404(ProductionPlant, pk=data_for_prod_pl)
        except:
            raise IndexError(f'нет такого завода в id {data_for_prod_pl}')
        retail_nw = RetailNetwork.objects.create(title=data_for_retail_nw, supplier=prod_pl)
        Contact.objects.create(**data_for_contact, retail_network=retail_nw)
        return retail_nw

    def update(self, instance, validated_data):
        try:
            instance.title = validated_data.get("title", instance.title)
            new_email = validated_data.get('contact').get('email')
            new_country = validated_data.get('contact').get('country')
            new_city = validated_data.get('contact').get('city')
            new_street = validated_data.get('contact').get('street')
            new_number_home = validated_data.get('contact').get('number_home')
            supplier_id = validated_data.get('supplier').get('title')
            supplier = get_object_or_404(ProductionPlant, pk=supplier_id)
        except:
            raise ValueError('Некорректные данные')
        instance.supplier = supplier
        instance.contact.email = new_email
        instance.contact.country = new_country
        instance.contact.city = new_city
        instance.contact.street = new_street
        instance.contact.number_home = new_number_home
        instance.contact.retail_network_id = validated_data.get("contact.retail_network_id",
                                                                instance.contact.retail_network_id)
        instance.save()
        return instance

    class Meta:
        model = RetailNetwork
        fields = ('title', 'contact', 'supplier')
