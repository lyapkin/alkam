from rest_framework import serializers

from .models import *



class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    categories = ArticleCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    categories = ArticleCategorySerializer(read_only=True, many=True)
    content_preview = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ("content",)

    def get_content_preview(self, article):
        return article.content[:100]


