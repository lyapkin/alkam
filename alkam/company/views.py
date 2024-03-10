from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *

# Create your views here.
class AboutApi(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = About.objects.all()
    serializer_class = AboutSerializer