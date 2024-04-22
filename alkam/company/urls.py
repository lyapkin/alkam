from django.urls import path, include
from rest_framework import routers


from .views import AboutApi, ProjectApi, CooperationApi, SpecialOfferApi

router = routers.SimpleRouter()
router.register('about', AboutApi)
router.register('projects', ProjectApi)
router.register('cooperation', CooperationApi)
router.register('specialoffer', SpecialOfferApi)

urlpatterns = [
    path('', include(router.urls)),
]