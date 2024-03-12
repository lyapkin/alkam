import re
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *
        

class CallApi(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class CommercialOfferApi(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = CommercialOffer.objects.all()
    serializer_class = CommercialOfferSerializer
