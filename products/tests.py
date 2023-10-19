from rest_framework.test import APITestCase
from rest_framework import status

from users.models import CustomUser
from .models import Product

class ProductTestCase(APITestCase):

    def setUp(self):
        user_data = {'username': 'alexandr', 'password': '123qwe'}
        self.user = CustomUser.objects.create(**user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        data_product = {'title': 'product', 'model': 'model', 'release': '2022-01-01'}
        response = self.client.post(f'/products/create/', data=data_product)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(Product.objects.all().first().title, 'product')

    def test_detail_product(self):
        data_product = {'title': 'product', 'model': 'model', 'release': '2022-01-01'}
        product = Product.objects.create(**data_product)
        response = self.client.get(f'/products/detail/{product.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(Product.objects.all().first().title, 'product')


    def test_deleteil_product(self):
        data_product = {'title': 'product', 'model': 'model', 'release': '2022-01-01'}
        product = Product.objects.create(**data_product)
        response = self.client.delete(f'/products/delete/{product.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Product.objects.all().count(), 0)


    def test_update_product(self):
        data_product = {'title': 'product', 'model': 'model', 'release': '2022-01-01'}
        product = Product.objects.create(**data_product)
        data_product = {'title': 'update_product', 'model': 'update_model', 'release': '2022-01-02'}
        response = self.client.put(f'/products/update/{product.pk}/', data=data_product)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(Product.objects.all().first().title, 'update_product')