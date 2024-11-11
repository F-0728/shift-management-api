from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransportationFeeViewSet

router = DefaultRouter()
router.register('transportation_fees', TransportationFeeViewSet)

urlpatterns = router.urls
