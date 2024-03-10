from django.urls import path, include
from rest_framework import routers


from .views import AboutApi

router = routers.SimpleRouter()
router.register(r'', AboutApi)

urlpatterns = [
    path('about/', include(router.urls)),
]