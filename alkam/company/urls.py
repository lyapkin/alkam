from django.urls import path, include
from rest_framework import routers


from .views import AboutApi, ProjectApi, CooperationApi, SpecialOfferApi, Slider1Api, Slider2Api

router = routers.SimpleRouter()
router.register('about', AboutApi)
router.register('projects', ProjectApi)
router.register('cooperation', CooperationApi)
router.register('specialoffer', SpecialOfferApi)
router.register('slider1', Slider1Api)
router.register('slider2', Slider2Api)

urlpatterns = [
    path('', include(router.urls)),
]