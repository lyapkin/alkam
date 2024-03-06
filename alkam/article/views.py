from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *


class ArticleApiPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 50

    def get_paginated_response(self, data):
        querysetCategories = ArticleCategory.objects.all()
        serializerCategory = ArticleCategorySerializer(querysetCategories, many=True)
        return Response({
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "count": self.page.paginator.count,
            "result": data,
            "categories": serializerCategory.data
        })

class ArticleApi(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    serializers_action_classes = {
        "list": ArticleListSerializer,
        "retrieve": ArticleSerializer
    }
    pagination_class = ArticleApiPagination

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializers_action_classes[self.action]
        if self.action == "retrieve":
            return self.serializers_action_classes[self.action]

    def get_queryset(self):
        queryset = Article.objects.order_by("-id")

        category_slug = self.request.query_params.get("category")
        if category_slug is not None:
            category = ArticleCategory.objects.filter(slug=category_slug)
            if category.count() == 0: return Article.objects.none()

            queryset = queryset.filter(categories=category[0])

        return queryset

    @action(detail=False)
    def categories(self, request):
        categories = ArticleCategory.objects.all()
        serializer = ArticleCategorySerializer(categories, many=True)
        return Response(serializer.data)

