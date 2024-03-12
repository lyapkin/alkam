from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.SimpleRouter()
router.register('calls', CallApi)
router.register('commercials', CommercialOfferApi)

urlpatterns = [
    path('', include(router.urls)),
]