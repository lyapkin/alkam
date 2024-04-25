from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
class AboutApi(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class CooperationApi(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Cooperation.objects.all()
    serializer_class = CooperationSerializer


class SpecialOfferApi(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = SpecialOffers.objects.all()
    serializer_class = OffersSerializer

    def list(self, request, *args, **kwargs):
        response_obj = {
            "description": SpecialOfferDescription.objects.get(id=1),
            "offers": self.get_queryset()
        }
        return Response(self.get_serializer_class()(response_obj, context={'request': request}).data)


class ProjectApi(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.order_by('-id')
    serializer_action_classes = {
        "retrieve": ProjectSerializer,
        "list": ProjectListSerializer
    }

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]
    

class Slider1Api(viewsets.ReadOnlyModelViewSet):
    queryset = Slider1.objects.order_by('-id')
    serializer_class = Slider1Serializer


class Slider2Api(viewsets.ReadOnlyModelViewSet):
    queryset = Slider2.objects.order_by('-id')
    serializer_class = Slider2Serializer