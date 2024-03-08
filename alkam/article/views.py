from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *


class ArticleApi(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    queryset = Article.objects.order_by("-id")
    serializer_action_classes = {
        "list": ArticlePreviewSerializer,
        "retrieve": ArticleSerializer
    }

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]
    
    def list(self, request, *args, **kwargs):
        response_obj = {
            "articles": self.get_queryset(),
            "categories": ArticleCategory.objects.all()
        }
        return Response(ArticleCategoriesListSerializer(response_obj).data)



