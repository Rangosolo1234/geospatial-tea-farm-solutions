from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from .views import register_user

router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'farms', views.FarmViewSet)
router.register(r'deliveries', views.DailyTeaDeliveryViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'centers', views.TeaCollectionCenterViewSet)
router.register(r'trucks', views.TruckLocationViewSet)
router.register(r'weather', views.WeatherDataViewSet)
router.register(r'soil', views.SoilDataViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),        # POST /api/register/
    path('login/', TokenObtainPairView.as_view(), name='login'),  # POST /api/login/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]