from django.urls import reverse
from mock import MagicMock
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from auto_catalog.models import VehicleModel, Automaker


class VehicleModelTests(APITransactionTestCase):

    def setUp(self):

        self.automaker = Automaker.objects.create(name='xxx', country='yyy')
        user = MagicMock()
        user.is_authenticated.return_value = True
        self.client.force_authenticate(user)

    def tearDown(self):

        VehicleModel.objects.all().delete()
        Automaker.objects.all().delete()

    def test_create_vehiclemodel(self):
        url = '/api/vehiclemodels/'
        data = {
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker.id,
            'name': 'Uno'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VehicleModel.objects.count(), 1)
        self.assertEqual(VehicleModel.objects.get().name, data['name'])
        self.assertEqual(VehicleModel.objects.get().automaker.id, self.automaker.id)
        self.assertEqual(VehicleModel.objects.get().vehicle_type, VehicleModel.VehicleType.CAR)

    def test_create_vehiclemodel_incomplete(self):
        url = '/api/vehiclemodels/'
        data = {
            'name': 'Uno',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_vehiclemodels(self):
        from auto_catalog.fixture_util import create_vehicle_models

        create_vehicle_models(10)

        url = '/api/vehiclemodels/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

        for item in response.json():

            self.assert_(isinstance(item['id'], int))
            self.assert_(isinstance(item['name'], str))
            self.assert_(len(item['name']) > 0)
            self.assert_(isinstance(item['automaker'], int))
            self.assert_(isinstance(item['vehicle_type'], int))

    def test_update_vehiclemodel(self):

        d = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })

        url = f'/api/vehiclemodels/{d.id}/'
        data = {
            'vehicle_type': VehicleModel.VehicleType.MOTORCYCLE,
            'automaker': self.automaker.id,
            'name': 'Uno'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['vehicle_type'], VehicleModel.VehicleType.MOTORCYCLE)
        self.assertEqual(response.json()['name'], 'Uno')

    def test_update_vehiclemodel_incomplete(self):
        d = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })

        url = f'/api/vehiclemodels/{d.id}/'
        data = {
            'vehicle_type': VehicleModel.VehicleType.MOTORCYCLE,
            'automaker': self.automaker.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_vehiclemodel(self):
        d = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })

        url = f'/api/vehiclemodels/{d.id}/'
        data = {
            'vehicle_type': VehicleModel.VehicleType.MOTORCYCLE,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['vehicle_type'], VehicleModel.VehicleType.MOTORCYCLE)
        self.assertEqual(response.json()['name'], 'Uno')

    def test_partial_update_vehiclemodel_empty(self):
        d = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })

        url = f'/api/vehiclemodels/{d.id}/'
        data = {}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['vehicle_type'], VehicleModel.VehicleType.CAR)
        self.assertEqual(response.json()['name'], 'Uno')

    def test_delete_vehiclemodel(self):
        d = VehicleModel.objects.create(**{
            'vehicle_type': VehicleModel.VehicleType.CAR,
            'automaker': self.automaker,
            'name': 'Uno'
        })

        url = f'/api/vehiclemodels/{d.id}/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(VehicleModel.DoesNotExist):
            dd = VehicleModel.objects.get(id=d.id)

    def test_delete_vehiclemodel_doesnt_exist(self):

        url = f'/api/vehiclemodels/99999/'
        data = {}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


