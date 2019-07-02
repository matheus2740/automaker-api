from django.db import models
from django_uuid_upload import upload_to_uuid

# Create your models here.
from auto_catalog.choices import ChoicesMeta


class Automaker(models.Model):

    name = models.CharField('Automaker Name', max_length=64)
    country = models.CharField('Country of Origin', max_length=64)


class VehicleModel(models.Model):

    class VehicleType(metaclass=ChoicesMeta):

        # Some basic vehicle types, including Car and Motorcycle.
        CAR = 1
        MOTORCYCLE = 2
        SUV = 3
        TRUCK = 4

    vehicle_type = models.IntegerField('Vehicle Type', choices=VehicleType)

    automaker = models.ForeignKey(Automaker, on_delete=models.PROTECT, verbose_name='Automaker')

    name = models.CharField('Model Name', max_length=64)

    stock_photo = models.ImageField(
        'Stock Photo of the Model',
        upload_to=upload_to_uuid('models_pictures'),
        default='models_pictures/no_image.png'
    )


class Vehicle(models.Model):

    # NOTE:
    # Automaker and vehicle type are omitted here, because vehicle model already defines these relationships.
    # Its not possible to have the same model in different automakers.
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT, verbose_name='Vehicle Model')

    # NOTE:
    # Color is not as simple as it may seem at first. For it's implementation, we have some choices:
    # 1. Foreign key to a `AutoColor(name : str, hue : rgb value, sample : image)` table;
    # 2. IntegerField with a Choices definition, for some basic colors)
    # 3. Char/TextField manually populated with the color name.
    # The complexity arises from the fact that automakers do not have a standard for car colors.
    # The same color can have different names for different models, different models can have
    # different colors, and the problem only gets worse between automakers.
    # If we are going for a generic/rough color definition (maybe it doesn't matter that much for the application),
    # then an IntegerField+Choices or FK would do. However, if accuracy is desired,
    # first we have to acknowledge that color will change over time, so Int+Choices is not adequate.
    # Second, we must assess if we can possibly have a definition for all the colors and its name.
    # Maybe they are available through the automakers's site/api, or maybe not.
    # At any rate, this decision should be careful, and discussion with the team, and analisys of
    # business requirements are certainly very helpful.
    # For the purposes of this challenge, I chose the CharField route, as it will give a lot
    # of flexibility, and the business requirements are not 100% clear.
    color = models.CharField('Vehicle Color', max_length=64)

    # NOTE:
    # The word mileage may give the impression of the unit of measure being 'Miles',
    # but it is also used for kilometers in metric countries (such as Canada).
    mileage = models.IntegerField('Vehicle mileage (in KM)')

    engine_volume = models.IntegerField('Engine Volume (in milliliters)')

    vanity_photo = models.ImageField('Stock Photo of the Model', upload_to=upload_to_uuid('vanity_pictures'), null=True)
