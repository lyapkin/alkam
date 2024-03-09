from django.urls import path, include
from rest_framework import routers


from .views import ContactsApi

# router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'', ContactsApi.as_view(), basename="contacts")

urlpatterns = [
    path('', ContactsApi.as_view()),
]