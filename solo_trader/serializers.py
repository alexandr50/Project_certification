from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from production_plant.models import ProductionPlant
from production_plant.serializers import ProductionPlantSerializer
from products.models import Product
from products.serializers import ProductSerializer
from retail_network.models import RetailNetwork
from retail_network.serializers import RetailNetworkForSoloSerializer
from solo_trader.models import SoleTrader


class SoloTraderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    supplier_pd = ProductionPlantSerializer()
    supplier_rt = RetailNetworkForSoloSerializer()

    class Meta:
        model = SoleTrader
        fields = ('title', 'contact', 'supplier_pd', 'supplier_rt')


class SoleTraderCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    suppl_pd = serializers.CharField(allow_null=True, allow_blank=True)
    suppl_rt = serializers.CharField(allow_blank=True, allow_null=True)
    products = ProductSerializer(many=True, required=False)

    def create(self, validated_data):
        data_for_contact = validated_data.pop('contact')
        data_for_solo_tr = validated_data.pop('title')
        debt = validated_data.pop('debt')
        data_for_supplier_pd = validated_data.pop('suppl_pd')
        data_for_supplier_rt = validated_data.pop('suppl_rt')
        data_for_product = validated_data.pop('products')
        if data_for_supplier_pd:

            data_for_supplier_pd = int(data_for_supplier_pd)
            prod_pl = ProductionPlant.objects.get(id=data_for_supplier_pd)
            solo_tr = SoleTrader.objects.create(title=data_for_solo_tr, debt=debt, supplier_pd=prod_pl)

        elif data_for_supplier_rt:

            data_for_supplier_rt = int(data_for_supplier_rt)
            retail = RetailNetwork.objects.get(id=data_for_supplier_rt)
            solo_tr = SoleTrader.objects.create(title=data_for_solo_tr, supplier_rt=retail)

        Contact.objects.create(**data_for_contact, solo_trader=solo_tr)
        for prod in data_for_product:
            Product.objects.create(**prod)
        return solo_tr

    class Meta:
        model = SoleTrader
        fields = ('title', 'contact', 'suppl_pd', 'suppl_rt', 'products', 'debt')


class SoloTraderUpdateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    suppl_pd = serializers.CharField(allow_null=True, allow_blank=True)
    suppl_rt = serializers.CharField(allow_blank=True, allow_null=True)

    def update(self, instance, validated_data):

        instance.title = validated_data.get("title", instance.title)
        new_email = validated_data.get('contact').get('email')
        new_country = validated_data.get('contact').get('country')
        new_city = validated_data.get('contact').get('city')
        new_street = validated_data.get('contact').get('street')
        new_number_home = validated_data.get('contact').get('number_home')

        id_suppl_pd = validated_data.get('suppl_pd')
        id_suppl_rt = validated_data.get('suppl_rt')
        if id_suppl_pd:
            suppl_pd = ProductionPlant.objects.get(id=id_suppl_pd)
            instance.supplier_pd = suppl_pd
            instance.supplier_rt = None
        elif id_suppl_rt:
            suppl_rt = RetailNetwork.objects.get(id=id_suppl_rt)
            instance.supplier_rt = suppl_rt
            instance.supplier_pd = None

        instance.contact.email = new_email
        instance.contact.country = new_country
        instance.contact.city = new_city
        instance.contact.street = new_street
        instance.contact.number_home = new_number_home
        instance.contact.save()
        instance.save()
        return instance

    class Meta:
        model = SoleTrader
        fields = ('title', 'contact', 'suppl_pd', 'suppl_rt')
