from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class TestCustomUser(APITestCase):
    def setUp(self):
        user_data = {'username': 'alexandr', 'password': '123qwe'}
        self.user = CustomUser.objects.create(**user_data)
        self.client.force_authenticate(user=self.user)

    def test_detail_user(self):
        response = self.client.get(f'/users/detail/{self.user.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response.json()['username'], self.user.username)

    def test_create_user(self):
        user_data = {'username': 'alexandr_test', 'password': '123qwe', 'first_name': 'alex'}
        response = self.client.post('/users/create/', data=user_data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED, )
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(CustomUser.objects.all()[1].username, 'alexandr_test')

    def test_update_user(self):
        data = {'username': 'username', 'password': '123qwe'}
        user = CustomUser.objects.create(**data)
        update_data = {'username': 'update_username', 'password': '123qwe'}
        response = self.client.put(f'/users/update/{user.pk}/', data=update_data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(CustomUser.objects.get(pk=user.pk).username, 'update_username')

    def test_delete_user(self):
        data = {'username': 'username', 'password': '123qwe'}
        user = CustomUser.objects.create(**data)
        response = self.client.delete(f'/users/delete/{user.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(CustomUser.objects.all().count(), 1)
