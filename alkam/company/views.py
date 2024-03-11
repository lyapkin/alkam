from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *

# Create your views here.
class AboutApi(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ProjectApi(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_action_classes = {
        "retrieve": ProjectSerializer,
        "list": ProjectListSerializer
    }

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]