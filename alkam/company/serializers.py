from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers
from django.conf import settings

from .models import *


class TextFieldSerializer(serializers.Field):
    def to_representation(self, value):
        domain = 'http://'+str(get_current_site(self.context['request']))
        if self.context['request'].is_secure():
            domain = 'https://'+str(get_current_site(self.context['request']))
        text = value.replace("src=\"/media/", f"src=\"{domain}/media/")
        return text


class AboutSerializer(serializers.ModelSerializer):
    text = TextFieldSerializer()
    class Meta:
        model = About
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    content = TextFieldSerializer()

    class Meta:
        model = Project
        fields = ("id", "content")


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "preview", "preview_image")