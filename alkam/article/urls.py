from django.urls import path, include
from rest_framework import routers


from .views import ArticleApi
from product.views import ProductApi

router = routers.SimpleRouter()
router.register(r'', ArticleApi)

urlpatterns = [
    path('', include(router.urls)),
]