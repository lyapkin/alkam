from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers
from django.conf import settings

from .models import *


class TextFieldSerializer(serializers.Field):
    def to_representation(self, value):
        domain = 'http://'+str(get_current_site(self.context['request']))
        if self.context['request'].is_secure():
            domain = 'https://'+str(get_current_site(self.context['request']))
        content = value.replace("src=\"/media/", f"src=\"{domain}/media/")
        content = content.replace("&lt;", "<")
        content = content.replace("&gt;", ">")
        content = content.replace("&quot;", "")
        return content


class AboutSerializer(serializers.ModelSerializer):
    text = TextFieldSerializer()
    class Meta:
        model = About
        fields = "__all__"


class CooperationSerializer(serializers.ModelSerializer):
    metaltraders = TextFieldSerializer()
    enterprises = TextFieldSerializer()
    class Meta:
        model = Cooperation
        fields = "__all__"


class SpecialOfferDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOfferDescription
        fields = "__all__"


class SpecialOffersSerializer(serializers.ModelSerializer):
    text = TextFieldSerializer()
    class Meta:
        model = SpecialOffers
        exclude = ('title',)


class OffersSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "description": SpecialOfferDescriptionSerializer(instance["description"]).data,
            "offers": SpecialOffersSerializer(instance["offers"], many=True, context={'request': self.context['request']}).data
        }


class ProjectSerializer(serializers.ModelSerializer):
    content = TextFieldSerializer()

    class Meta:
        model = Project
        fields = ("id", "content")


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "preview", "preview_image")


class Slider1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Slider1
        fields = '__all__'


class Slider2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Slider2
        fields = '__all__'