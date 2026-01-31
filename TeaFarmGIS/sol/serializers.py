from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create a user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

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
    farmer_details = FarmerSerializer(source='farmer', read_only=True)
    
    class Meta:
        model = DailyTeaDelivery
        fields = [
            'id', 
            'farmer', 
            'farmer_details',
            'date', 
            'quantity_kg', 
            'plucking_labour_cost'
        ]
        extra_kwargs = {
            'farmer': {'write_only': True}
        }


class ExpenseSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    farmer = FarmerSerializer(source='farm.farmer', read_only=True)
    
    class Meta:
        model = Expense
        fields = [
            'id',
            'farm', 
            'farm_name',
            'farmer',  # full farmer object
            'date', 
            'expense_type', 
            'amount'
        ]

# class ExpenseSerializer(serializers.ModelSerializer):
#     # farm_name = serializers.CharField(source='farm.name', read_only=True)
#     class Meta:
#         model = Expense
#         fields = '__all__'

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