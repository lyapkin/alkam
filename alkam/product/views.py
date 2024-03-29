from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *

class ProductAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    
class ProductApi(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    pagination_class = ProductAPIListPagination

    def list(self, request, *args, **kwargs):
        if "grouped" in request.query_params:
            return self.group()
        
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.order_by("-id")

        query_params = self.request.query_params
        if "grouped" in query_params:
            return queryset

        alloy_slug = query_params.get("alloy")
        if alloy_slug is not None and alloy_slug != "all":
            alloy_type = AlloyType.objects.filter(slug=alloy_slug)
            if alloy_type.count() == 0: return Product.objects.none()

            queryset = queryset.filter(alloy_type=alloy_type[0])

        category_slug = query_params.get("category")
        if category_slug is not None and category_slug != "all":
            category = ProductCategory.objects.filter(slug=category_slug)
            if category.count() == 0: return Product.objects.none()

            queryset = queryset.filter(product_category=category[0])

        material_slug = query_params.get("material")
        if material_slug is not None and material_slug != "all":
            material = ProductMaterial.objects.filter(slug=material_slug)
            if material.count() == 0: return Product.objects.none()

            queryset = queryset.filter(material=material[0])

        return queryset

    @action(detail=False)
    def filters_list(self, request):
        alloys = AlloyType.objects.order_by("-id")
        alloysSerializer = AlloyTypeSerializer(alloys, many=True)
        categories = ProductCategory.objects.order_by("-id")
        categoriesSerializer = ProductCategorySerializer(categories, many=True)
        materials = ProductMaterial.objects.order_by("-id")
        materialsSerializer = ProductMaterialSerializer(materials, many=True)
        result = {
            "alloys": alloysSerializer.data,
            "categories": categoriesSerializer.data,
            "materials": materialsSerializer.data
        }
        return Response(result)
    
    def group(self):
        queryset = ProductCategory.objects.order_by("-id")
        products = []
        for t in queryset:
            product_item = {}
            product_item["typeSlug"] = t.slug
            product_item["typeName"] = t.name
            product_item["products"] = ProductSerializer(t.products.order_by("-id"), many=True).data
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
            product_item["products"] = ProductPreviewSerializer(t.products.all()[:5], many=True).data
            products.append(product_item)
        return Response(products)