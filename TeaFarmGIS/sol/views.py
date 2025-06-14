from rest_framework import viewsets
from .models import *
from .serializers import *

#======================Creating viewsets==================================
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class DailyTeaDeliveryViewSet(viewsets.ModelViewSet):
    queryset = DailyTeaDelivery.objects.all()
    serializer_class = DailyTeaDeliverySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class TeaCollectionCenterViewSet(viewsets.ModelViewSet):
    queryset = TeaCollectionCenter.objects.all()
    serializer_class = TeaCollectionCenterSerializer

class TruckLocationViewSet(viewsets.ModelViewSet):
    queryset = TruckLocation.objects.all()
    serializer_class = TruckLocationSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class SoilDataViewSet(viewsets.ModelViewSet):
    queryset = SoilData.objects.all()
    serializer_class = SoilDataSerializer

