from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters


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
    permission_classes = [IsAuthenticated]
  
class FarmerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'phone']

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']

class DailyTeaDeliveryViewSet(viewsets.ModelViewSet):
    queryset = DailyTeaDelivery.objects.all().select_related('farmer')
    serializer_class = DailyTeaDeliverySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['farmer', 'date']
    search_fields = ['farmer__first_name', 'farmer__last_name']
    ordering_fields = ['date', 'quantity_kg']
    
    def get_queryset(self):
        # Only show deliveries for farmers the user is associated with
        user = self.request.user
        if user.groups.filter(name='Farmers').exists():
            return DailyTeaDelivery.objects.filter(farmer__user=user)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        # Automatically associate with farmer if user is a farmer
        user = self.request.user
        if user.groups.filter(name='Farmers').exists():
            farmer = Farmer.objects.get(user=user)
            serializer.save(farmer=farmer)
        else:
            serializer.save()

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['farm']

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

