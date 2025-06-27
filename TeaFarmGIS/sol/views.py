from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User created successfully'}, status=201)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow signup from unauthenticated users


    
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

