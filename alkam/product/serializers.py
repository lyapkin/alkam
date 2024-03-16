from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    product_category = serializers.StringRelatedField()
    supply_condition = serializers.StringRelatedField()
    alloy_type = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    material = serializers.StringRelatedField()

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
            "length",
            "material"
        )
    

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class AlloyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlloyType
        fields = "__all__"


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = "__all__"


class ProductPreviewSerializer(serializers.ModelSerializer):
    product_category = serializers.StringRelatedField()
    alloy_type = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    material = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            "id",
            "product_category",
            "alloy_type",
            "standard",
            "material"
        )