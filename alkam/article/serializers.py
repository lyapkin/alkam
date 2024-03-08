from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "content", "date")

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        exclude = ("slug",)

class ArticlePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ("content",)


class ArticleCategoriesListSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "articles": ArticlePreviewSerializer(instance["articles"], many=True).data,
            "categories": ArticleCategorySerializer(instance["categories"], many=True).data
        }





