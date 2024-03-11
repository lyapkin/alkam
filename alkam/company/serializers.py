from rest_framework import serializers
from django.conf import settings

from .models import *


class TextFieldSerializer(serializers.Field):
    def to_representation(self, value):
        text = value.replace("src=\"/media/", f"src=\"{settings.SITE_DOMAIN}/media/")
        return text


class AboutSerializer(serializers.ModelSerializer):
    text = TextFieldSerializer()
    class Meta:
        model = About
        fields = "__all__"