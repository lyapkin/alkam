from django.urls import path, include
from rest_framework import routers


from .views import ProductApi, ProductGroupedByCategoryApi

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', ProductApi)

urlpatterns = [
    path('', include(router.urls)),
    path('grouped/', ProductGroupedByCategoryApi.as_view(), name="products_grouped")
]