from django.urls import path, include
from rest_framework import routers


from .views import AboutApi, ProjectApi

router = routers.SimpleRouter()
router.register('about', AboutApi)
router.register('projects', ProjectApi)

urlpatterns = [
    path('', include(router.urls)),
]