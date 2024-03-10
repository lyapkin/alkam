from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    thickness = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    length = serializers.SerializerMethodField()
    product_category = serializers.StringRelatedField()
    supply_condition = serializers.StringRelatedField()
    alloy_type = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "id",
            "product_category",
            "supply_condition",
            "alloy_type",
            "standard",
            "thickness",
            "width",
            "length"
        )

    def get_thickness(self, product):
        return "{}-{}".format(product.thickness_min, product.thickness_max)
    
    def get_width(self, product):
        return "{}-{}".format(product.width_min, product.width_max)
    
    def get_length(self, product):
        return "{}-{}".format(product.length_min, product.length_max)
    

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class AlloyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlloyType
        fields = "__all__"


class ProductPreviewSerializer(serializers.ModelSerializer):
    product_category = serializers.StringRelatedField()
    alloy_type = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "id",
            "product_category",
            "alloy_type",
            "standard",
        )