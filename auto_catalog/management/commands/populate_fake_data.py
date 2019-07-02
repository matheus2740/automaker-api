from django.core.management.base import BaseCommand

from auto_catalog.fixture_util import create_automakers, create_vehicle_models, create_vehicles


class Command(BaseCommand):
    help = 'Create fake data and insert it into the database.'

    def handle(self, *args, **options):

        create_automakers(10)
        create_vehicle_models(50),
        create_vehicles(200)
