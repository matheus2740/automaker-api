from django_filters import rest_framework as filters
from rest_framework import viewsets, serializers

from auto_catalog.models import Automaker, VehicleModel, Vehicle


# region Automaker


class AutomakerFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    country = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Automaker
        fields = ('name', 'country')


class AutomakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Automaker
        fields = ('id', 'name', 'country')


class AutomakerViewSet(viewsets.ModelViewSet):
    queryset = Automaker.objects.all()
    serializer_class = AutomakerSerializer
    filter_class = AutomakerFilters
    ordering = ('-id',)


# endregion Automaker


# region VehicleModel


class VehicleModelFilters(filters.FilterSet):
    vehicle_type = filters.ChoiceFilter(choices=VehicleModel.VehicleType)
    automaker = filters.ModelChoiceFilter(queryset=Automaker.objects.all())
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = VehicleModel
        fields = ('vehicle_type', 'automaker', 'name')


class VehicleModelSerializer(serializers.ModelSerializer):

    automaker_name = serializers.ReadOnlyField(source='automaker.name')

    class Meta:
        model = VehicleModel
        fields = ('id', 'vehicle_type', 'automaker', 'automaker_name', 'name', 'stock_photo')
        read_only_fields = ('stock_photo', )


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    filter_class = VehicleModelFilters
    ordering = ('-id',)


# endregion VehicleModel


# region Vehicle


class VehicleFilters(filters.FilterSet):
    model = filters.ModelChoiceFilter(queryset=VehicleModel.objects.all())
    color = filters.CharFilter(lookup_expr='icontains')
    mileage = filters.NumberFilter()
    mileage__gte = filters.NumberFilter(name='mileage', lookup_expr='gte')
    mileage__lte = filters.NumberFilter(name='mileage', lookup_expr='lte')
    engine_volume = filters.NumberFilter()
    engine_volume__gte = filters.NumberFilter(name='engine_volume', lookup_expr='gte')
    engine_volume__lte = filters.NumberFilter(name='engine_volume', lookup_expr='lte')
    model_name = filters.CharFilter(name='model__name', lookup_expr='icontains')
    automaker = filters.ModelChoiceFilter(name='model__automaker', queryset=Automaker.objects.all())
    automaker_name = filters.CharFilter(name='model__automaker__name', lookup_expr='icontains')
    vehicle_type = filters.ChoiceFilter(name='model__vehicle_type', choices=VehicleModel.VehicleType)

    class Meta:
        model = Vehicle
        fields = ('model', 'color', 'mileage', 'engine_volume', 'model_name', 'automaker', 'vehicle_type')


class VehicleSerializer(serializers.ModelSerializer):

    model = VehicleModelSerializer(read_only=True)
    model_id = serializers.IntegerField()

    class Meta:
        model = Vehicle
        fields = ('id', 'model', 'model_id', 'color', 'mileage', 'engine_volume', 'vanity_photo')
        read_only_fields = ('vanity_photo',)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_class = VehicleFilters
    ordering = ('-id',)


# endregion Vehicle
