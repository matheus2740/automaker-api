import random

from auto_catalog.models import Automaker, VehicleModel, Vehicle
from auto_catalog.random_words import gen_word


def create_automakers(amount):

    ADJECTIVES = {
        'Bob\'s',
        'Alice\'s',
        'Popular',
        'Richman\'s',
        'Gordon\'s',
        'Rick\'s',
        'Blue',
        'Yellow',
        'Green',
        'Amazing'
    }

    SUBSTANTIVES = {
        'Vehicles',
        'Automobiles',
        'Motors',
        'Transportation',
        'Cars',
        'Luxury & Engines',
        'Locomotion',
    }
    COUNTRIES = {
        'Brazil',
        'United States',
        'France',
        'Germany',
        'Japan',
        'Korea',
        'China',
        'Czech Republic',
        'United Kingdom',
        'Italy'
    }

    for i in range(amount):

        adjective = random.sample(ADJECTIVES, 1)[0]
        substantive = random.sample(SUBSTANTIVES, 1)[0]

        Automaker.objects.create(
            name=f'{adjective} {substantive}',
            country=random.sample(COUNTRIES, 1)[0]
        )


def create_vehicle_models(amount):

    AUTOMAKERS = list(Automaker.objects.all())

    for i in range(amount):

        VehicleModel.objects.create(
            vehicle_type=random.randint(1, 4),
            automaker=random.sample(AUTOMAKERS, 1)[0],
            name=gen_word(2, 4)
        )


def create_vehicles(amount):

    VEHICLE_MODELS = list(VehicleModel.objects.all())

    COLORS = {
        'Red',
        'Yellow',
        'Green',
        'Blue',
        'Silver',
        'Black',
        'White',
        'Space Green',
        'Marble Fuchsia',
        'Autumn Orange',
        'Cherry Red',
        'Athens Silver',
        'Golden Gold',
        'Alien Purple'
    }

    for i in range(amount):

        Vehicle.objects.create(
            model=random.sample(VEHICLE_MODELS, 1)[0],
            color=random.sample(COLORS, 1)[0],
            mileage=random.randint(10000, 150000),
            engine_volume=random.randint(150, 5000)
        )
