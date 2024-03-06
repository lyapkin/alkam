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

    @action(detail=False)
    def categories(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def alloys(self, request):
        categories = AlloyType.objects.all()
        serializer = AlloyTypeSerializer(categories, many=True)
        return Response(serializer.data)


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