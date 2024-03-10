from rest_framework import serializers

from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("region", "city", "address", "map")


class TelephoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelphoneNumber
        fields = ("number",)


class DepartmentSerializer(serializers.ModelSerializer):
    telephone_number = serializers.StringRelatedField()

    class Meta:
        model = Department
        fields = "__all__"



class ContactsSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        departaments = instance["departaments"]
        addresses = instance["addresses"]

        result = {
            "departments": DepartmentSerializer(departaments, many=True).data,
            "address": AddressSerializer(addresses[0]).data if addresses.count() > 0 else None
        }

        return result