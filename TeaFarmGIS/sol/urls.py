from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'farms', views.FarmViewSet)
router.register(r'deliveries', views.DailyTeaDeliveryViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'centers', views.TeaCollectionCenterViewSet)
router.register(r'trucks', views.TruckLocationViewSet)
router.register(r'weather', views.WeatherDataViewSet)
router.register(r'soil', views.SoilDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
