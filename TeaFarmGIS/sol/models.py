from django.db import models
from django.contrib.gis.db import models as gis_models

from django.contrib.auth.models import User
# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='Unknown')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Farm(gis_models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    boundary = gis_models.PolygonField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Farm"

class DailyTeaDelivery(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateField()
    quantity_kg = models.FloatField()
    plucking_labour_cost = models.FloatField()

class Expense(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    date = models.DateField()
    expense_type = models.CharField(max_length=50)
    amount = models.FloatField()
   
class TeaCollectionCenter(gis_models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PointField()

class TruckLocation(gis_models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = gis_models.PointField() 
    tea_center = models.ForeignKey(TeaCollectionCenter, on_delete=models.CASCADE)

class WeatherData(gis_models.Model):
    location = gis_models.PointField()
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    rainfall = models.FloatField()

class SoilData(gis_models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    ph = models.FloatField()
    moisture = models.FloatField()