from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *

class ProductAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 50
    
class ProductApi(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductAPIListPagination

    def list(self, request, *args, **kwargs):
        if "grouped" in request.query_params:
            return self.group()
        
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()

        query_params = self.request.query_params
        if "grouped" in query_params:
            return queryset

        alloy_slug = query_params.get("alloy")
        if alloy_slug is not None:
            alloy_type = AlloyType.objects.filter(slug=alloy_slug)
            if alloy_type.count() == 0: return Product.objects.none()

            queryset = queryset.filter(alloy_type=alloy_type[0])

        category_slug = query_params.get("category")
        if category_slug is not None:
            category = ProductCategory.objects.filter(slug=category_slug)
            if category.count() == 0: return Product.objects.none()

            queryset = queryset.filter(product_category=category[0])

        return queryset

    @action(detail=False)
    def filters_list(self, request):
        alloys = AlloyType.objects.all()
        alloysSerializer = AlloyTypeSerializer(alloys, many=True)
        categories = ProductCategory.objects.all()
        categoriesSerializer = ProductCategorySerializer(categories, many=True)
        result = {
            "alloys": alloysSerializer.data,
            "categories": categoriesSerializer.data
        }
        return Response(result)
    
    def group(self):
        queryset = ProductCategory.objects.all()
        products = []
        for t in queryset:
            product_item = {}
            product_item["typeSlug"] = t.slug
            product_item["typeName"] = t.name
            product_item["products"] = ProductSerializer(t.products.all(), many=True).data
            products.append(product_item)
        return Response(products)


class ProductGroupedByCategoryApi(generics.ListAPIView):
     queryset = ProductCategory.objects.all()
    
     def list(self, request):
        products = []
        for t in self.get_queryset():
            product_item = {}
            product_item["typeSlug"] = t.slug
            product_item["typeName"] = t.name
            product_item["products"] = ProductSerializer(t.products.all()[:5], many=True).data
            products.append(product_item)
        return Response(products)