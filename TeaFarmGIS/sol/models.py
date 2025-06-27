from django.db import models
from django.contrib.gis.db import models  #For geospatial model fields and geometries

from django.contrib.auth.models import User #Importing User that comes by default when app is initialized

# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='Unknown')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Farm(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    boundary = models.PolygonField()

    def __str__(self):
        return self.name

class DailyTeaDelivery(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateField()
    quantity_kg = models.FloatField()
    plucking_labour_cost = models.FloatField()

class Expense(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    date = models.DateField()
    expense_type = models.CharField(max_length=50)  # fertilizer, weeding
    amount = models.FloatField()

class TeaCollectionCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

class TruckLocation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.PointField()
    tea_center = models.ForeignKey(TeaCollectionCenter, on_delete=models.CASCADE)

class WeatherData(models.Model):
    location = models.PointField()
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    rainfall = models.FloatField()

class SoilData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    ph = models.FloatField()
    moisture = models.FloatField()