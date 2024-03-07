from rest_framework import serializers

from .models import *



class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ("categories", "slug", "image_url", "content_concise")


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ("content",)





