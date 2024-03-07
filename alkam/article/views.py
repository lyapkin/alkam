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
    serializer_class = ArticleSerializer
    serializers_action_classes = {
        "list": ArticleListSerializer,
        "retrieve": ArticleSerializer
    }

    def list(self, request, *args, **kwargs):
        articles = self.get_queryset()
        categories = ArticleCategory.objects.all()
        cats = {}
        for cat in categories.values():
            cats[cat["id"]] = cat["name"]
        articles_serializer = ArticleListSerializer(articles, many=True)
        return Response({"articles": articles_serializer.data, "categories": cats})


