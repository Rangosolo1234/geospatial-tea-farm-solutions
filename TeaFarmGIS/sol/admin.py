from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin

from .models import (
    Farmer,
    Farm,
    DailyTeaDelivery,
    Expense,
    TeaCollectionCenter,
    TruckLocation,
    WeatherData,
    SoilData
)


# Register your models here.
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone')

@admin.register(Farm)
class FarmAdmin(LeafletGeoAdmin):
    list_display = ('name', 'farmer')

@admin.register(DailyTeaDelivery)
class DailyTeaDeliveryAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'date', 'quantity_kg', 'plucking_labour_cost')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('farm', 'date', 'expense_type', 'amount')

@admin.register(TeaCollectionCenter)
class TeaCollectionCenterAdmin(LeafletGeoAdmin):
    list_display = ('name',)

@admin.register(TruckLocation)
class TruckLocationAdmin(LeafletGeoAdmin):
    list_display = ('tea_center', 'timestamp')

@admin.register(WeatherData)
class WeatherDataAdmin(LeafletGeoAdmin):
    list_display = ('timestamp', 'temperature', 'rainfall')

@admin.register(SoilData)
class SoilDataAdmin(admin.ModelAdmin):
    list_display = ('farm', 'ph', 'moisture')