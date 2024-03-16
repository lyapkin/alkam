import re
from rest_framework import serializers

from .models import *
    

class CommonSerializer(serializers.ModelSerializer):

    def validate_number(self, number):
        result = re.match(r'(^[\+][0-9]{1}[0-9]{3}[0-9]{7}$)', number)
        if result is None:
            raise serializers.ValidationError('Номер телефона должен быть в форме: +79876543210; укажите код города, если необходимо')
        return number


class CallSerializer(CommonSerializer):
    class Meta:
        model = Call
        exclude = ('date',)


class CommercialOfferSerializer(CommonSerializer):
    class Meta:
        model = CommercialOffer
        exclude = ('date',)





