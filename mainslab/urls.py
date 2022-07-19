from django.urls import path
from .viewsets import BillViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'bills', BillViewSet, basename='bills')

urlpatterns = [
    path('api/', include(router.urls)),
]
