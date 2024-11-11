from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaryViewSet

router = DefaultRouter()
router.register('salaries', SalaryViewSet)

urlpatterns = router.urls
