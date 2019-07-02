from django.urls import reverse
from mock import MagicMock
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from auto_catalog.models import Automaker


class AutomakerTests(APITransactionTestCase):

    def setUp(self):
        user = MagicMock()
        user.is_authenticated.return_value = True
        self.client.force_authenticate(user)

    def tearDown(self):

        Automaker.objects.all().delete()

    def test_create_automaker(self):
        url = '/api/automakers/'
        data = {
            'name': 'Fiat',
            'country': 'Italy'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Automaker.objects.count(), 1)
        self.assertEqual(Automaker.objects.get().name, data['name'])
        self.assertEqual(Automaker.objects.get().country, data['country'])

    def test_create_automaker_incomplete(self):
        url = '/api/automakers/'
        data = {
            'name': 'Fiat',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_automakers(self):
        from auto_catalog.fixture_util import create_automakers

        create_automakers(10)

        url = '/api/automakers/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

        for item in response.json():

            self.assert_(isinstance(item['id'], int))
            self.assert_(isinstance(item['name'], str))
            self.assert_(len(item['name']) > 0)
            self.assert_(isinstance(item['country'], str))
            self.assert_(len(item['country']) > 0)

    def test_update_automaker(self):

        d = Automaker.objects.create(name='xxx', country='yyy')

        url = f'/api/automakers/{d.id}/'
        data = {
            'name': 'xxx',
            'country': 'zzz'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'xxx')
        self.assertEqual(response.json()['country'], 'zzz')

    def test_update_automaker_incomplete(self):

        d = Automaker.objects.create(name='xxx', country='yyy')

        url = f'/api/automakers/{d.id}/'
        data = {
            'name': 'xxx',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_automaker(self):

        d = Automaker.objects.create(name='xxx', country='yyy')

        url = f'/api/automakers/{d.id}/'
        data = {
            'country': 'zzz'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'xxx')
        self.assertEqual(response.json()['country'], 'zzz')

    def test_partial_update_automaker_empty(self):

        d = Automaker.objects.create(name='xxx', country='yyy')

        url = f'/api/automakers/{d.id}/'
        data = {}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'xxx')
        self.assertEqual(response.json()['country'], 'yyy')

    def test_delete_automaker(self):

        d = Automaker.objects.create(name='xxx', country='yyy')

        url = f'/api/automakers/{d.id}/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Automaker.DoesNotExist):
            dd = Automaker.objects.get(id=d.id)

    def test_delete_automaker_doesnt_exist(self):

        url = f'/api/automakers/99999/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


