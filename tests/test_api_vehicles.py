from django.urls import reverse
from mock import MagicMock
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from auto_catalog.models import VehicleModel, Automaker, Vehicle


class VehicleTests(APITransactionTestCase):

    def setUp(self):

        self.automaker = Automaker.objects.create(name='xxx', country='yyy')
        self.vmodel = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })
        user = MagicMock()
        user.is_authenticated.return_value = True
        self.client.force_authenticate(user)

    def tearDown(self):

        Vehicle.objects.all().delete()
        VehicleModel.objects.all().delete()
        Automaker.objects.all().delete()

    def test_create_vehicle(self):
        url = '/api/vehicles/'
        data = {
            'model_id': self.vmodel.id,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 1)
        self.assertEqual(Vehicle.objects.get().model.id, self.vmodel.id)
        self.assertEqual(Vehicle.objects.get().color, 'Black')
        self.assertEqual(Vehicle.objects.get().mileage, 1234)
        self.assertEqual(Vehicle.objects.get().engine_volume, 1234)

    def test_create_vehicle_incomplete(self):
        url = '/api/vehicles/'
        data = {
            'model_id': self.vmodel.id,
            'color': 'Black',
            'mileage': 1234,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_vehicles(self):
        from auto_catalog.fixture_util import create_vehicles

        create_vehicles(10)

        url = '/api/vehicles/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

        for item in response.json():

            self.assert_(isinstance(item['id'], int))
            self.assert_(isinstance(item['model'], dict))
            self.assert_(isinstance(item['model_id'], int))
            self.assert_(isinstance(item['color'], str))
            self.assert_(len(item['color']) > 0)
            self.assert_(isinstance(item['mileage'], int))
            self.assert_(isinstance(item['engine_volume'], int))

    def test_update_vehicle(self):

        d = Vehicle.objects.create(**{
            'model': self.vmodel,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        })

        url = f'/api/vehicles/{d.id}/'
        data = {
            'model_id': self.vmodel.id,
            'color': 'Black',
            'mileage': 5432,
            'engine_volume': 5432,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['model_id'], self.vmodel.id)
        self.assertEqual(response.json()['color'], 'Black')
        self.assertEqual(response.json()['mileage'], 5432)
        self.assertEqual(response.json()['engine_volume'], 5432)

    def test_update_vehicle_incomplete(self):
        d = Vehicle.objects.create(**{
            'model': self.vmodel,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        })

        url = f'/api/vehicles/{d.id}/'
        data = {
            'model_id': self.vmodel.id,
            'color': 'Black',
            'mileage': 5432,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_vehicle(self):
        d = Vehicle.objects.create(**{
            'model': self.vmodel,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        })

        url = f'/api/vehicles/{d.id}/'
        data = {
            'engine_volume': 5432,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['model_id'], self.vmodel.id)
        self.assertEqual(response.json()['color'], 'Black')
        self.assertEqual(response.json()['mileage'], 1234)
        self.assertEqual(response.json()['engine_volume'], 5432)

    def test_partial_update_vehicle_empty(self):
        d = Vehicle.objects.create(**{
            'model': self.vmodel,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        })

        url = f'/api/vehicles/{d.id}/'
        data = {}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['model_id'], self.vmodel.id)
        self.assertEqual(response.json()['color'], 'Black')
        self.assertEqual(response.json()['mileage'], 1234)
        self.assertEqual(response.json()['engine_volume'], 1234)

    def test_delete_vehicle(self):
        d = Vehicle.objects.create(**{
            'model': self.vmodel,
            'color': 'Black',
            'mileage': 1234,
            'engine_volume': 1234,
        })

        url = f'/api/vehicles/{d.id}/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Vehicle.DoesNotExist):
            dd = Vehicle.objects.get(id=d.id)

    def test_delete_vehicle_doesnt_exist(self):

        url = f'/api/vehicles/99999/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


