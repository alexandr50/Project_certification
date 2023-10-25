from rest_framework import status
from rest_framework.test import APITestCase

from contacts.models import Contact
from production_plant.models import ProductionPlant
from users.models import CustomUser
from .models import RetailNetwork


class RetailNetworkTestCase(APITestCase):

    def setUp(self):
        user_data = {'username': 'alexandr', 'password': '123qwe'}
        data_contact = {'email': 'test@mail.ru',
                        'country': 'Russia',
                        'city': 'Ivanovo',
                        'street': 'teststreet',
                        'number_home': '12'}
        data_contact_sup = {'email': 'test@mail1.ru',
                        'country': 'Russia1',
                        'city': 'Ivanovo1',
                        'street': 'teststreet1',
                        'number_home': '121'}
        data_retail = {'title': 'retail'}
        data_pr_pl = {'title': 'pr_pl'}
        self.user = CustomUser.objects.create(**user_data)
        self.contact = Contact.objects.create(**data_contact)
        self.contact_s = Contact.objects.create(**data_contact_sup)
        self.retail = RetailNetwork.objects.create(**data_retail)
        self.supplier = ProductionPlant.objects.create(**data_pr_pl)
        self.client.force_authenticate(user=self.user)

    # def test_create_retail(self):
    #     data_retail = {'title': 'retail',
    #                    'debt': 1,
    #                    'contact':
    #                       {'email': 'test@mail.ru',
    #                        'country': 'Russia',
    #                        'city': 'Ivanovo',
    #                        'street': 'teststreet',
    #                        'number_home': '12'},
    #                    'products':
    #                       [{'title': 'product',
    #                         'model': 'model',
    #                         'release': '2022-01-01'}],
    #                    'supplier':
    #                        {'title': 'pr_pl',
    #                         'contact':
    #                             {'email': 'test@mail1.ru',
    #                              'country': 'Russia1',
    #                              'city': 'Ivanovo1',
    #                              'street': 'teststreet1',
    #                              'number_home': '121'}
    #                         }}
    #     response = self.client.post(f'/retail_networks/create/', data=data_retail, format='json')
    #     print(response.json())
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )
    #     self.assertEqual(RetailNetwork.objects.all().count(), 2)
    #     self.assertEqual(RetailNetwork.objects.all().first().title, 'retail')

    def test_detail_retail(self):
        response = self.client.get(f'/retail_networks/detail/{self.retail.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(RetailNetwork.objects.all().count(), 1)
        self.assertEqual(RetailNetwork.objects.all().first().title, 'retail')

    def test_delete_retail(self):
        response = self.client.delete(f'/retail_networks/delete/{self.retail.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(RetailNetwork.objects.all().count(), 0)

    # def test_update_product(self):
    #     data_update = {'title': 'retail',
    #                    'debt': 2,
    #                    'contact':
    #                       {'email': 'test@mail2.ru',
    #                        'country': 'Russia2',
    #                        'city': 'Ivanovo2',
    #                        'street': 'teststreet2',
    #                        'number_home': '122'},
    #                    'products':
    #                       [{'title': 'product2',
    #                         'model': 'model2',
    #                         'release': '2022-01-02'}],
    #                    'supplier':
    #                        {'title': 'supplier2'}}
    #     response = self.client.put(f'/retail_networks/update/{self.retail.pk}/', data=data_update, format='json')
    #     print(response.json())
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(RetailNetwork.objects.all().count(), 1)
    #     self.assertEqual(RetailNetwork.objects.all().first().title, 'update')
