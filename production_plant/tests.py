from rest_framework import status
from rest_framework.test import APITestCase

from contacts.models import Contact
from users.models import CustomUser
from .models import ProductionPlant


class ProductTestCase(APITestCase):

    def setUp(self):
        user_data = {'username': 'alexandr', 'password': '123qwe'}
        data_contact = {'email': 'test@mail.ru',
                        'country': 'Russia',
                        'city': 'Ivanovo',
                        'street': 'teststreet',
                        'number_home': '12'}
        data_pr_pl = {'title': 'pr_pl'}
        self.user = CustomUser.objects.create(**user_data)
        self.contact = Contact.objects.create(**data_contact)
        self.pr_pl = ProductionPlant.objects.create(**data_pr_pl)
        self.client.force_authenticate(user=self.user)

    def test_create_pr_pl(self):
        data_pr_pl = {'title': 'pr_pl',
                      'contact':
                          {'email': 'test@mail.ru',
                           'country': 'Russia',
                           'city': 'Ivanovo',
                           'street': 'teststreet',
                           'number_home': '12'},
                      'products':
                          [{'title': 'product',
                            'model': 'model',
                            'release': '2022-01-01'}]}
        response = self.client.post(f'/production_plant/create/', data=data_pr_pl, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(ProductionPlant.objects.all().count(), 2)
        self.assertEqual(ProductionPlant.objects.all().first().title, 'pr_pl')

    def test_detail_pr_pl(self):
        response = self.client.get(f'/production_plant/detail/{self.pr_pl.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(ProductionPlant.objects.all().count(), 1)
        self.assertEqual(ProductionPlant.objects.all().first().title, 'pr_pl')

    def test_deleteil_product(self):
        response = self.client.delete(f'/production_plant/delete/{self.pr_pl.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(ProductionPlant.objects.all().count(), 0)

    def test_update_product(self):
        data_update = {'title': 'update'}
        response = self.client.put(f'/production_plant/update/{self.pr_pl.pk}/', data=data_update)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(ProductionPlant.objects.all().count(), 1)
        self.assertEqual(ProductionPlant.objects.all().first().title, 'update')
