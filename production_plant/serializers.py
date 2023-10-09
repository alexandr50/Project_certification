from rest_framework import serializers

from production_plant.models import ProductionPlant


class ProductionPlantSerializer(serializers.ModelSerializer):
    # contact = ContactSerializer()
    #
    # def create(self, validated_data):
    #     data_for_contact = validated_data.pop('contact')
    #     data_for_prod_pl = validated_data.pop('title')
    #     prod_plant = ProductionPlant.objects.create(title=data_for_prod_pl)
    #     Contact.objects.create(**data_for_contact, production_plant=prod_plant)
    #     return prod_plant
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.contact.email = validated_data.get("title", instance.contact.email)
    #     instance.contact.country = validated_data.get("title", instance.contact.country)
    #     instance.contact.city = validated_data.get("title", instance.contact.city)
    #     instance.contact.street = validated_data.get("title", instance.contact.street)
    #     instance.contact.nuber_home = validated_data.get("title", instance.contact.number_home)
    #     instance.contact.production_plant_id = validated_data.get("title", instance.contact.production_plant_id)
    #     instance.save()
    #     return instance

    class Meta:
        model = ProductionPlant
        fields = ('title', 'email', 'country', 'city', 'street', 'number_home')
