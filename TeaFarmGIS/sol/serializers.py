from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class FarmSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Farm
        geo_field = 'boundary'  # PolygonField
        fields = ('id', 'name', 'farmer', 'boundary')

class DailyTeaDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTeaDelivery
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class TeaCollectionCenterSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TeaCollectionCenter
        geo_field = 'location'  # PointField
        fields = ('id', 'name', 'location')

class TruckLocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TruckLocation
        geo_field = 'location'  # PointField
        fields = ('id', 'location', 'timestamp', 'tea_center')

class WeatherDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WeatherData
        geo_field = 'location'
        fields = ('id', 'location', 'timestamp', 'temperature', 'rainfall')

class SoilDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilData
        fields = '__all__'