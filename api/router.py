from .views import ClientListViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientview',ClientListViewset, basename='clientview')